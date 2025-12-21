#!/usr/bin/env python3
"""
PDF Signature Detection Script for FileOrganizer

Checks PDFs for digital signatures and provides heuristics for signature detection.

Usage:
    python3 pdf_signature_check.py <pdf_path>                    # Check single PDF
    python3 pdf_signature_check.py --compare <pdf1> <pdf2>       # Compare two PDFs
    python3 pdf_signature_check.py --json <pdf_path>             # JSON output

Dependencies:
    pip install pypdf
"""

import argparse
import json
import os
import sys

try:
    import pypdf
except ImportError:
    print("Error: pypdf not installed. Run: pip install pypdf", file=sys.stderr)
    sys.exit(1)


def has_digital_signature(pdf_path: str) -> bool:
    """
    Check if a PDF has a digital signature.

    Returns True if the PDF contains a cryptographic digital signature.
    Does NOT detect image-based (scanned) signatures.
    """
    try:
        reader = pypdf.PdfReader(pdf_path)
        root = reader.trailer.get("/Root", {})

        # Check for AcroForm with signature flags
        if "/AcroForm" in root:
            acroform = root["/AcroForm"]
            if "/SigFlags" in acroform:
                sig_flags = int(acroform["/SigFlags"])
                # Bit 1 (value 1) = SignaturesExist
                return bool(sig_flags & 1)

        return False
    except Exception as e:
        print(f"Error reading PDF: {e}", file=sys.stderr)
        return False


def get_page_count(pdf_path: str) -> int:
    """Get the number of pages in a PDF."""
    try:
        reader = pypdf.PdfReader(pdf_path)
        return len(reader.pages)
    except Exception:
        return -1


def signature_heuristic(pdf1: str, pdf2: str) -> dict:
    """
    Compare two PDFs to detect possible signature differences.

    Returns a dict with:
    - pages_match: bool
    - size_diff_percent: float
    - likely_signed: str (path of likely signed version, or None)
    - reason: str
    """
    size1 = os.path.getsize(pdf1)
    size2 = os.path.getsize(pdf2)
    pages1 = get_page_count(pdf1)
    pages2 = get_page_count(pdf2)

    pages_match = pages1 == pages2
    size_diff = abs(size2 - size1) / min(size1, size2) if min(size1, size2) > 0 else 0

    result = {
        "pdf1": {"path": pdf1, "size": size1, "pages": pages1},
        "pdf2": {"path": pdf2, "size": size2, "pages": pages2},
        "pages_match": pages_match,
        "size_diff_percent": round(size_diff * 100, 1),
        "likely_signed": None,
        "reason": ""
    }

    # Check digital signatures first
    sig1 = has_digital_signature(pdf1)
    sig2 = has_digital_signature(pdf2)
    result["pdf1"]["has_digital_signature"] = sig1
    result["pdf2"]["has_digital_signature"] = sig2

    if sig1 and not sig2:
        result["likely_signed"] = pdf1
        result["reason"] = "Has digital signature"
    elif sig2 and not sig1:
        result["likely_signed"] = pdf2
        result["reason"] = "Has digital signature"
    elif pages_match and size_diff > 0.15:
        # Same pages but >15% size difference - may have image signature
        larger = pdf1 if size1 > size2 else pdf2
        result["likely_signed"] = larger
        result["reason"] = f"Same page count, {result['size_diff_percent']}% larger (may have signature)"

    return result


def analyze_pdf(pdf_path: str) -> dict:
    """Analyze a single PDF for signature and metadata."""
    return {
        "path": pdf_path,
        "exists": os.path.exists(pdf_path),
        "size_bytes": os.path.getsize(pdf_path) if os.path.exists(pdf_path) else 0,
        "size_human": format_size(os.path.getsize(pdf_path)) if os.path.exists(pdf_path) else "0",
        "pages": get_page_count(pdf_path),
        "has_digital_signature": has_digital_signature(pdf_path)
    }


def format_size(size_bytes: int) -> str:
    """Format bytes as human-readable size."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.0f}{unit}" if unit == "B" else f"{size_bytes:.1f}{unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f}TB"


def main():
    parser = argparse.ArgumentParser(description="Check PDFs for digital signatures")
    parser.add_argument("pdf", nargs="?", help="PDF file to check")
    parser.add_argument("--compare", nargs=2, metavar=("PDF1", "PDF2"),
                        help="Compare two PDFs for signature differences")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.compare:
        result = signature_heuristic(args.compare[0], args.compare[1])
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"PDF 1: {result['pdf1']['path']}")
            print(f"  Size: {format_size(result['pdf1']['size'])}, Pages: {result['pdf1']['pages']}")
            print(f"  Digital Signature: {'Yes' if result['pdf1']['has_digital_signature'] else 'No'}")
            print(f"\nPDF 2: {result['pdf2']['path']}")
            print(f"  Size: {format_size(result['pdf2']['size'])}, Pages: {result['pdf2']['pages']}")
            print(f"  Digital Signature: {'Yes' if result['pdf2']['has_digital_signature'] else 'No'}")
            print(f"\nPages Match: {'Yes' if result['pages_match'] else 'No'}")
            print(f"Size Difference: {result['size_diff_percent']}%")
            if result['likely_signed']:
                print(f"\n→ Likely signed version: {result['likely_signed']}")
                print(f"  Reason: {result['reason']}")

    elif args.pdf:
        result = analyze_pdf(args.pdf)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"File: {result['path']}")
            print(f"Size: {result['size_human']}")
            print(f"Pages: {result['pages']}")
            print(f"Digital Signature: {'Yes' if result['has_digital_signature'] else 'No'}")

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
