"""OCR integration using AWS Textract for scanned PDF processing."""

import boto3
import time
from pathlib import Path
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()


class TextractOCR:
    """AWS Textract OCR processor for scanned bank statements."""

    def __init__(
        self,
        aws_access_key: Optional[str] = None,
        aws_secret_key: Optional[str] = None,
        region: Optional[str] = None
    ):
        """Initialize Textract client."""
        self.client = boto3.client(
            "textract",
            aws_access_key_id=aws_access_key or os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=aws_secret_key or os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=region or os.getenv("AWS_REGION", "ap-southeast-1")
        )

    def extract_from_pdf(self, pdf_path: Path) -> dict:
        """
        Extract text and tables from a PDF file.

        Returns a dict with:
        - text: Full extracted text
        - tables: List of extracted tables (each as list of rows)
        - pages: Number of pages processed
        """
        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()

        # For multi-page PDFs, use async API
        # For simplicity in V1, we use sync API (works for PDFs up to ~10 pages)
        response = self.client.analyze_document(
            Document={"Bytes": pdf_bytes},
            FeatureTypes=["TABLES"]
        )

        return self._parse_response(response)

    def extract_from_pdf_async(self, pdf_path: Path, s3_bucket: str, s3_key: str) -> dict:
        """
        Extract from large PDFs using async API (requires S3).

        For V1 POC, we'll use the sync API. This is here for future use.
        """
        # Upload to S3 first
        s3 = boto3.client("s3")
        with open(pdf_path, "rb") as f:
            s3.upload_fileobj(f, s3_bucket, s3_key)

        # Start async job
        response = self.client.start_document_analysis(
            DocumentLocation={
                "S3Object": {
                    "Bucket": s3_bucket,
                    "Name": s3_key
                }
            },
            FeatureTypes=["TABLES"]
        )

        job_id = response["JobId"]

        # Poll for completion
        while True:
            response = self.client.get_document_analysis(JobId=job_id)
            status = response["JobStatus"]

            if status == "SUCCEEDED":
                break
            elif status == "FAILED":
                raise Exception(f"Textract job failed: {response.get('StatusMessage')}")

            time.sleep(5)

        return self._parse_response(response)

    def _parse_response(self, response: dict) -> dict:
        """Parse Textract response into structured data."""
        blocks = response.get("Blocks", [])

        # Build block ID map
        block_map = {block["Id"]: block for block in blocks}

        # Extract full text
        text_lines = []
        for block in blocks:
            if block["BlockType"] == "LINE":
                text_lines.append(block.get("Text", ""))

        full_text = "\n".join(text_lines)

        # Extract tables
        tables = []
        for block in blocks:
            if block["BlockType"] == "TABLE":
                table = self._extract_table(block, block_map)
                if table:
                    tables.append(table)

        # Count pages
        page_count = max(
            (block.get("Page", 1) for block in blocks),
            default=1
        )

        return {
            "text": full_text,
            "tables": tables,
            "pages": page_count,
            "raw_blocks": blocks  # Keep raw for debugging
        }

    def _extract_table(self, table_block: dict, block_map: dict) -> list[list[str]]:
        """Extract a table as a 2D list of cell values."""
        rows = {}

        # Get all cells in this table
        if "Relationships" not in table_block:
            return []

        for relationship in table_block.get("Relationships", []):
            if relationship["Type"] == "CHILD":
                for cell_id in relationship["Ids"]:
                    cell = block_map.get(cell_id)
                    if cell and cell["BlockType"] == "CELL":
                        row_idx = cell.get("RowIndex", 1) - 1
                        col_idx = cell.get("ColumnIndex", 1) - 1

                        # Get cell text
                        cell_text = self._get_cell_text(cell, block_map)

                        if row_idx not in rows:
                            rows[row_idx] = {}
                        rows[row_idx][col_idx] = cell_text

        # Convert to 2D list
        if not rows:
            return []

        max_row = max(rows.keys())
        max_col = max(max(cols.keys()) for cols in rows.values())

        table = []
        for r in range(max_row + 1):
            row = []
            for c in range(max_col + 1):
                row.append(rows.get(r, {}).get(c, ""))
            table.append(row)

        return table

    def _get_cell_text(self, cell: dict, block_map: dict) -> str:
        """Get text content of a cell."""
        text_parts = []

        for relationship in cell.get("Relationships", []):
            if relationship["Type"] == "CHILD":
                for child_id in relationship["Ids"]:
                    child = block_map.get(child_id)
                    if child and child["BlockType"] == "WORD":
                        text_parts.append(child.get("Text", ""))

        return " ".join(text_parts)


def extract_text_from_pdf(pdf_path: Path) -> dict:
    """
    Convenience function to extract text and tables from a PDF.

    Returns:
        dict with keys: text, tables, pages
    """
    ocr = TextractOCR()
    return ocr.extract_from_pdf(pdf_path)


def format_tables_as_text(tables: list[list[list[str]]]) -> str:
    """
    Format extracted tables as readable text for Claude parsing.

    Args:
        tables: List of tables, each table is a list of rows

    Returns:
        Formatted string representation of all tables
    """
    output = []

    for i, table in enumerate(tables, 1):
        output.append(f"=== TABLE {i} ===")

        if not table:
            output.append("(empty table)")
            continue

        # Calculate column widths
        col_widths = []
        for col_idx in range(len(table[0])):
            max_width = max(len(str(row[col_idx])) for row in table if col_idx < len(row))
            col_widths.append(min(max_width, 50))  # Cap at 50 chars

        # Format rows
        for row in table:
            formatted_row = []
            for col_idx, cell in enumerate(row):
                if col_idx < len(col_widths):
                    formatted_row.append(str(cell)[:50].ljust(col_widths[col_idx]))
            output.append(" | ".join(formatted_row))

        output.append("")

    return "\n".join(output)


if __name__ == "__main__":
    # Test with a sample PDF
    import sys

    if len(sys.argv) < 2:
        print("Usage: python ocr.py <pdf_path>")
        sys.exit(1)

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        print(f"File not found: {pdf_path}")
        sys.exit(1)

    print(f"Processing: {pdf_path}")
    result = extract_text_from_pdf(pdf_path)

    print(f"\n=== EXTRACTED TEXT ({result['pages']} pages) ===\n")
    print(result["text"][:2000])  # First 2000 chars

    print(f"\n=== EXTRACTED TABLES ({len(result['tables'])} tables) ===\n")
    print(format_tables_as_text(result["tables"]))
