"""Claude-powered parser for extracting position data from OCR output."""

import json
import os
from datetime import date
from typing import Optional
from dataclasses import dataclass, asdict
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()


@dataclass
class ExtractedPosition:
    """A single extracted position from a bank statement."""
    isin: str
    security_name: Optional[str] = None
    cusip: Optional[str] = None
    issuer: Optional[str] = None
    face_value: Optional[float] = None
    market_price: Optional[float] = None
    market_value: Optional[float] = None
    currency: Optional[str] = None
    coupon_rate: Optional[float] = None
    maturity_date: Optional[str] = None  # ISO format string
    accrued_interest: Optional[float] = None


@dataclass
class ExtractionResult:
    """Result of parsing a bank statement."""
    positions: list[ExtractedPosition]
    statement_date: Optional[str] = None  # ISO format string
    bank_name: Optional[str] = None
    account_number: Optional[str] = None
    total_value: Optional[float] = None
    currency: Optional[str] = None
    warnings: list[str] = None
    raw_response: str = None


EXTRACTION_PROMPT = """You are a financial data extraction specialist. Extract all bond/fixed income positions from this bank statement.

For each position, extract:
- isin: ISIN identifier (12 characters, starts with 2-letter country code)
- security_name: Full security name/description
- cusip: CUSIP if available (9 characters)
- issuer: Issuer name (company/government)
- face_value: Par/nominal/face value
- market_price: Current price (often as % of par, e.g., 98.5)
- market_value: Total market value
- currency: Currency code (USD, EUR, CHF, GBP, SGD, etc.)
- coupon_rate: Interest rate (as decimal, e.g., 4.5 for 4.5%)
- maturity_date: Maturity date in YYYY-MM-DD format
- accrued_interest: Accrued interest if shown

Also extract:
- statement_date: Statement date in YYYY-MM-DD format
- bank_name: Name of the bank
- account_number: Account number if visible
- total_value: Total portfolio value if shown
- currency: Base currency of the statement

IMPORTANT RULES:
1. Only extract positions with valid ISINs (12 characters, starts with country code like US, XS, DE, etc.)
2. If a value is unclear or missing, set it to null
3. Convert all percentages to decimals (4.5% → 4.5)
4. Dates must be in YYYY-MM-DD format
5. Face value and market value should be raw numbers without currency symbols
6. Include a "warnings" array for any data quality issues you notice

Return ONLY valid JSON in this exact format:
{
  "positions": [
    {
      "isin": "XS1234567890",
      "security_name": "Example Corp 4.5% 2028",
      "cusip": null,
      "issuer": "Example Corporation",
      "face_value": 100000,
      "market_price": 98.5,
      "market_value": 98500,
      "currency": "USD",
      "coupon_rate": 4.5,
      "maturity_date": "2028-06-15",
      "accrued_interest": 1250
    }
  ],
  "statement_date": "2024-11-30",
  "bank_name": "Example Bank",
  "account_number": "12345678",
  "total_value": 1500000,
  "currency": "USD",
  "warnings": ["Some positions may have unclear face values"]
}

Here is the bank statement content:

---
{content}
---

Extract all positions and return ONLY the JSON response."""


class StatementParser:
    """Parse bank statements using Claude."""

    def __init__(self, api_key: Optional[str] = None, model: str = "claude-sonnet-4-20250514"):
        """Initialize the parser."""
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))
        self.model = model

    def parse_statement(
        self,
        text: str,
        tables_text: Optional[str] = None,
        bank_hint: Optional[str] = None
    ) -> ExtractionResult:
        """
        Parse a bank statement and extract positions.

        Args:
            text: Raw text from OCR
            tables_text: Formatted table text from OCR
            bank_hint: Optional hint about which bank this is from

        Returns:
            ExtractionResult with extracted positions
        """
        # Combine text and tables
        content = text
        if tables_text:
            content += f"\n\n=== TABLES ===\n{tables_text}"

        if bank_hint:
            content = f"[This statement is from {bank_hint}]\n\n{content}"

        # Call Claude
        message = self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            messages=[
                {
                    "role": "user",
                    "content": EXTRACTION_PROMPT.format(content=content)
                }
            ]
        )

        raw_response = message.content[0].text

        # Parse JSON response
        try:
            # Handle potential markdown code blocks
            json_str = raw_response
            if "```json" in json_str:
                json_str = json_str.split("```json")[1].split("```")[0]
            elif "```" in json_str:
                json_str = json_str.split("```")[1].split("```")[0]

            data = json.loads(json_str.strip())
        except json.JSONDecodeError as e:
            return ExtractionResult(
                positions=[],
                warnings=[f"Failed to parse Claude response: {e}"],
                raw_response=raw_response
            )

        # Convert to dataclasses
        positions = []
        for pos_data in data.get("positions", []):
            # Validate ISIN
            isin = pos_data.get("isin")
            if not isin or len(isin) != 12:
                continue

            positions.append(ExtractedPosition(
                isin=isin,
                security_name=pos_data.get("security_name"),
                cusip=pos_data.get("cusip"),
                issuer=pos_data.get("issuer"),
                face_value=self._parse_float(pos_data.get("face_value")),
                market_price=self._parse_float(pos_data.get("market_price")),
                market_value=self._parse_float(pos_data.get("market_value")),
                currency=pos_data.get("currency"),
                coupon_rate=self._parse_float(pos_data.get("coupon_rate")),
                maturity_date=pos_data.get("maturity_date"),
                accrued_interest=self._parse_float(pos_data.get("accrued_interest"))
            ))

        return ExtractionResult(
            positions=positions,
            statement_date=data.get("statement_date"),
            bank_name=data.get("bank_name"),
            account_number=data.get("account_number"),
            total_value=self._parse_float(data.get("total_value")),
            currency=data.get("currency"),
            warnings=data.get("warnings", []),
            raw_response=raw_response
        )

    def _parse_float(self, value) -> Optional[float]:
        """Safely parse a float value."""
        if value is None:
            return None
        try:
            return float(value)
        except (ValueError, TypeError):
            return None


def parse_bank_statement(
    text: str,
    tables_text: Optional[str] = None,
    bank_hint: Optional[str] = None
) -> ExtractionResult:
    """
    Convenience function to parse a bank statement.

    Args:
        text: Raw text from OCR
        tables_text: Formatted table text from OCR
        bank_hint: Optional hint about which bank this is from

    Returns:
        ExtractionResult with extracted positions
    """
    parser = StatementParser()
    return parser.parse_statement(text, tables_text, bank_hint)


def positions_to_dict(positions: list[ExtractedPosition]) -> list[dict]:
    """Convert positions to list of dicts for JSON serialization."""
    return [asdict(p) for p in positions]


if __name__ == "__main__":
    # Test with sample text
    sample_text = """
    PORTFOLIO STATEMENT
    Bank: Example Private Bank
    Account: 12345678
    Statement Date: November 30, 2024

    FIXED INCOME HOLDINGS

    ISIN            Description                      Face Value    Price    Market Value    Currency
    XS2345678901    Credit Suisse 7.5% AT1 Perp     500,000       85.25    426,250         USD
    US123456789     JP Morgan 4.25% 2028            1,000,000     98.50    985,000         USD
    XS9876543210    Deutsche Bank 6.0% T2 2030      750,000       92.00    690,000         EUR

    Total Portfolio Value: 2,101,250 USD
    """

    print("Testing parser with sample text...")
    result = parse_bank_statement(sample_text)

    print(f"\nStatement Date: {result.statement_date}")
    print(f"Bank: {result.bank_name}")
    print(f"Positions found: {len(result.positions)}")

    for pos in result.positions:
        print(f"\n  {pos.isin}: {pos.security_name}")
        print(f"    Face Value: {pos.face_value} {pos.currency}")
        print(f"    Market Value: {pos.market_value}")

    if result.warnings:
        print(f"\nWarnings: {result.warnings}")
