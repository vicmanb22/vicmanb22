"""CLI interface for FamilyOfficeAnalytics."""

import click
from pathlib import Path
from datetime import date, datetime
import sys

from .database import (
    init_database,
    upsert_bank,
    upsert_security,
    insert_position,
    record_import,
    import_fx_rates_from_csv,
    convert_positions_to_usd,
    get_portfolio_summary,
)
from .ocr import extract_text_from_pdf, format_tables_as_text
from .parser import parse_bank_statement
from .enrichment import (
    generate_enrichment_request,
    import_enrichment_response,
    get_enrichment_status,
)
from .export import (
    generate_consolidation_report,
    generate_concentration_report,
    generate_port_export,
)
from .analytics import check_concentration_alerts


# Default paths
BASE_DIR = Path(__file__).parent.parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"
DATA_DIR = BASE_DIR / "data"


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """FamilyOfficeAnalytics - Extract and analyze fixed income positions from bank statements."""
    # Ensure database is initialized
    init_database()


@cli.command()
@click.argument("pdf_path", type=click.Path(exists=True, path_type=Path))
@click.option("--bank", "-b", required=True, help="Bank code (e.g., UBS, CS, JPM)")
@click.option("--bank-name", help="Full bank name (optional)")
@click.option("--statement-date", "-d", type=click.DateTime(formats=["%Y-%m-%d"]), help="Statement date (YYYY-MM-DD)")
def process(pdf_path: Path, bank: str, bank_name: str, statement_date: datetime):
    """Process a single PDF bank statement."""
    click.echo(f"Processing: {pdf_path}")
    click.echo(f"Bank: {bank}")

    # Register bank if needed
    upsert_bank(bank, bank_name or bank)

    # Step 1: OCR
    click.echo("  Extracting text with OCR...")
    try:
        ocr_result = extract_text_from_pdf(pdf_path)
        click.echo(f"  Extracted {ocr_result['pages']} pages, {len(ocr_result['tables'])} tables")
    except Exception as e:
        click.echo(f"  ERROR: OCR failed - {e}", err=True)
        record_import(bank, str(pdf_path), None, "ERROR", error_message=str(e))
        sys.exit(1)

    # Step 2: Parse with Claude
    click.echo("  Parsing positions with Claude...")
    tables_text = format_tables_as_text(ocr_result["tables"])
    try:
        parse_result = parse_bank_statement(
            ocr_result["text"],
            tables_text,
            bank_hint=bank_name or bank
        )
        click.echo(f"  Found {len(parse_result.positions)} positions")
    except Exception as e:
        click.echo(f"  ERROR: Parsing failed - {e}", err=True)
        record_import(bank, str(pdf_path), None, "ERROR", error_message=str(e))
        sys.exit(1)

    if parse_result.warnings:
        for warning in parse_result.warnings:
            click.echo(f"  WARNING: {warning}")

    # Determine statement date
    stmt_date = None
    if statement_date:
        stmt_date = statement_date.date()
    elif parse_result.statement_date:
        try:
            stmt_date = date.fromisoformat(parse_result.statement_date)
        except ValueError:
            pass

    if not stmt_date:
        click.echo("  WARNING: Could not determine statement date, using today")
        stmt_date = date.today()

    # Step 3: Store positions
    click.echo("  Storing positions in database...")
    positions_stored = 0

    for pos in parse_result.positions:
        # Ensure security exists
        mat_date = None
        if pos.maturity_date:
            try:
                mat_date = date.fromisoformat(pos.maturity_date)
            except ValueError:
                pass

        upsert_security(
            isin=pos.isin,
            name=pos.security_name,
            cusip=pos.cusip,
            issuer=pos.issuer,
            coupon_rate=pos.coupon_rate,
            maturity_date=mat_date,
            currency=pos.currency,
        )

        # Insert position
        insert_position(
            bank_code=bank,
            isin=pos.isin,
            statement_date=stmt_date,
            face_value=pos.face_value or 0,
            market_value=pos.market_value or 0,
            currency=pos.currency or "USD",
            source_file=str(pdf_path),
            market_price=pos.market_price,
        )
        positions_stored += 1

    # Record import
    record_import(
        bank_code=bank,
        filename=str(pdf_path),
        statement_date=stmt_date,
        status="COMPLETED",
        positions_extracted=positions_stored
    )

    click.echo(f"  Stored {positions_stored} positions")
    click.echo("Done!")


@cli.command("process-all")
@click.option("--input-dir", "-i", type=click.Path(exists=True, path_type=Path), default=INPUT_DIR)
def process_all(input_dir: Path):
    """Process all PDF files in the input directory."""
    pdf_files = list(input_dir.glob("*.pdf")) + list(input_dir.glob("*.PDF"))

    if not pdf_files:
        click.echo(f"No PDF files found in {input_dir}")
        return

    click.echo(f"Found {len(pdf_files)} PDF files")

    for pdf_path in pdf_files:
        # Try to extract bank code from filename (e.g., UBS_2024_11.pdf)
        parts = pdf_path.stem.split("_")
        bank = parts[0] if parts else "UNKNOWN"

        click.echo(f"\n{'='*50}")
        try:
            # Use Click's invoke to call process command
            ctx = click.get_current_context()
            ctx.invoke(process, pdf_path=pdf_path, bank=bank, bank_name=None, statement_date=None)
        except SystemExit:
            click.echo(f"Failed to process {pdf_path}")
            continue


@cli.command("enrich-request")
@click.option("--output", "-o", type=click.Path(path_type=Path), default=OUTPUT_DIR / "bloomberg_request.xlsx")
def enrich_request(output: Path):
    """Generate Bloomberg enrichment request file."""
    count = generate_enrichment_request(output)
    if count > 0:
        click.echo(f"Generated enrichment request with {count} securities: {output}")
        click.echo("\nNext steps:")
        click.echo("1. Open this file in Excel on Bloomberg Terminal")
        click.echo("2. Wait for BDP formulas to populate")
        click.echo("3. Save the file")
        click.echo("4. Run: foa enrich-import <saved_file.xlsx>")
    else:
        click.echo("No securities need enrichment")


@cli.command("enrich-import")
@click.argument("input_file", type=click.Path(exists=True, path_type=Path))
def enrich_import(input_file: Path):
    """Import enriched data from Bloomberg Excel file."""
    updated, errors = import_enrichment_response(input_file)
    click.echo(f"Imported enrichment data:")
    click.echo(f"  Updated: {updated}")
    click.echo(f"  Errors: {errors}")


@cli.command("enrich-status")
def enrich_status():
    """Show enrichment status."""
    status = get_enrichment_status()
    click.echo("Enrichment Status:")
    click.echo(f"  Total securities: {status['total_securities']}")
    click.echo(f"  Enriched: {status['enriched']}")
    click.echo(f"  Needs enrichment: {status['needs_enrichment']}")

    if status["by_security_type"]:
        click.echo("\nBy security type:")
        for item in status["by_security_type"]:
            click.echo(f"  {item['type'] or 'Unknown'}: {item['count']}")


@cli.command("fx-update")
@click.option("--file", "-f", type=click.Path(exists=True, path_type=Path), help="CSV file with FX rates")
@click.option("--rate", "-r", multiple=True, help="Manual rate: CCY=RATE (e.g., EUR=1.05)")
def fx_update(file: Path, rate: tuple):
    """Update FX rates from file or manual input."""
    from .database import upsert_fx_rate

    count = 0

    if file:
        count = import_fx_rates_from_csv(file)
        click.echo(f"Imported {count} FX rates from {file}")

    for r in rate:
        try:
            ccy, rate_val = r.split("=")
            upsert_fx_rate(ccy.strip().upper(), date.today(), float(rate_val))
            count += 1
            click.echo(f"Set {ccy.upper()} = {rate_val}")
        except ValueError:
            click.echo(f"Invalid rate format: {r} (expected CCY=RATE)", err=True)

    if count == 0:
        click.echo("No rates updated. Use --file or --rate options.")


@cli.command("fx-convert")
@click.option("--date", "-d", type=click.DateTime(formats=["%Y-%m-%d"]), help="Statement date to convert")
def fx_convert(date: datetime):
    """Convert positions to USD using stored FX rates."""
    stmt_date = date.date() if date else None

    if not stmt_date:
        # Use latest statement date
        from .database import get_connection
        conn = get_connection()
        result = conn.execute("SELECT MAX(statement_date) FROM positions").fetchone()
        conn.close()
        stmt_date = result[0] if result and result[0] else None

    if not stmt_date:
        click.echo("No positions found to convert")
        return

    count = convert_positions_to_usd(stmt_date)
    click.echo(f"Converted {count} positions to USD for {stmt_date}")


@cli.group()
def report():
    """Generate reports."""
    pass


@report.command("consolidation")
@click.option("--output", "-o", type=click.Path(path_type=Path), default=OUTPUT_DIR / "consolidation.xlsx")
def report_consolidation(output: Path):
    """Generate consolidation report."""
    count = generate_consolidation_report(output)
    click.echo(f"Generated consolidation report with {count} positions: {output}")


@report.command("concentration")
@click.option("--output", "-o", type=click.Path(path_type=Path), default=OUTPUT_DIR / "concentration.xlsx")
def report_concentration(output: Path):
    """Generate concentration risk report."""
    count = generate_concentration_report(output)
    click.echo(f"Generated concentration report with {count} alerts: {output}")


@report.command("all")
@click.option("--output-dir", "-o", type=click.Path(path_type=Path), default=OUTPUT_DIR)
def report_all(output_dir: Path):
    """Generate all reports."""
    output_dir.mkdir(parents=True, exist_ok=True)

    count1 = generate_consolidation_report(output_dir / "consolidation.xlsx")
    click.echo(f"Generated consolidation report: {count1} positions")

    count2 = generate_concentration_report(output_dir / "concentration.xlsx")
    click.echo(f"Generated concentration report: {count2} alerts")

    click.echo(f"\nReports saved to: {output_dir}")


@cli.group()
def export():
    """Export data."""
    pass


@export.command("port")
@click.option("--output", "-o", type=click.Path(path_type=Path), default=OUTPUT_DIR / "port_upload.csv")
def export_port(output: Path):
    """Export for Bloomberg PORT upload."""
    count = generate_port_export(output)
    click.echo(f"Generated PORT export with {count} positions: {output}")
    click.echo("\nTo upload to Bloomberg:")
    click.echo("1. Type PRTU in Bloomberg Terminal")
    click.echo("2. Select Import → CSV")
    click.echo(f"3. Choose {output}")


@cli.command("status")
def status():
    """Show portfolio status."""
    summary = get_portfolio_summary()

    click.echo("Portfolio Status")
    click.echo("=" * 40)
    click.echo(f"Total Positions: {summary.get('total_positions', 0)}")
    click.echo(f"Unique Securities: {summary.get('unique_securities', 0)}")
    click.echo(f"Banks: {summary.get('bank_count', 0)}")

    total_value = summary.get('total_value_usd')
    if total_value:
        click.echo(f"Total Value (USD): ${total_value:,.2f}")
    else:
        click.echo("Total Value (USD): Not calculated (run fx-convert)")

    # Check for alerts
    alerts = check_concentration_alerts()
    if alerts:
        click.echo(f"\nConcentration Alerts: {len(alerts)}")
        for alert in alerts[:5]:  # Show top 5
            click.echo(f"  [{alert.threshold_type.upper()}] {alert.category}: {alert.name} ({alert.exposure_pct:.1f}%)")
        if len(alerts) > 5:
            click.echo(f"  ... and {len(alerts) - 5} more")
    else:
        click.echo("\nNo concentration alerts")


@cli.command("init")
def init():
    """Initialize the database."""
    init_database()
    click.echo("Database initialized")
    click.echo(f"Location: {DATA_DIR / 'portfolio.duckdb'}")


if __name__ == "__main__":
    cli()
