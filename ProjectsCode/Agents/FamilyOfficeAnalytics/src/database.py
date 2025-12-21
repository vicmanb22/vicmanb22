"""CSV-based database operations for FamilyOfficeAnalytics."""

import pandas as pd
from pathlib import Path
from datetime import date, datetime
from typing import Optional
import os


# Default data directory
DEFAULT_DATA_DIR = Path(__file__).parent.parent / "data"

# CSV file paths
def _csv_path(name: str, data_dir: Optional[Path] = None) -> Path:
    """Get path to a CSV file."""
    dir_path = data_dir or DEFAULT_DATA_DIR
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path / f"{name}.csv"


# =============================================================================
# Initialization
# =============================================================================

def init_database(data_dir: Optional[Path] = None) -> None:
    """Initialize the CSV files with headers if they don't exist."""
    dir_path = data_dir or DEFAULT_DATA_DIR
    dir_path.mkdir(parents=True, exist_ok=True)

    # Banks
    banks_path = _csv_path("banks", dir_path)
    if not banks_path.exists():
        pd.DataFrame(columns=["code", "name"]).to_csv(banks_path, index=False)

    # Securities
    securities_path = _csv_path("securities", dir_path)
    if not securities_path.exists():
        pd.DataFrame(columns=[
            "isin", "cusip", "name", "issuer", "security_type", "payment_rank",
            "coupon_rate", "maturity_date", "currency", "rating_sp", "rating_moody",
            "modified_duration", "yield_to_maturity", "issuer_country", "issuer_sector",
            "last_enriched"
        ]).to_csv(securities_path, index=False)

    # Positions
    positions_path = _csv_path("positions", dir_path)
    if not positions_path.exists():
        pd.DataFrame(columns=[
            "id", "bank_code", "isin", "statement_date", "face_value",
            "market_price", "market_value", "market_value_usd", "currency",
            "source_file", "created_at"
        ]).to_csv(positions_path, index=False)

    # FX Rates
    fx_path = _csv_path("fx_rates", dir_path)
    if not fx_path.exists():
        pd.DataFrame(columns=["currency", "rate_date", "usd_rate"]).to_csv(fx_path, index=False)

    # Statement Imports
    imports_path = _csv_path("imports", dir_path)
    if not imports_path.exists():
        pd.DataFrame(columns=[
            "id", "bank_code", "filename", "statement_date", "status",
            "positions_extracted", "error_message", "processed_at", "created_at"
        ]).to_csv(imports_path, index=False)


def _read_csv(name: str, data_dir: Optional[Path] = None) -> pd.DataFrame:
    """Read a CSV file, returning empty DataFrame if it doesn't exist."""
    path = _csv_path(name, data_dir)
    if path.exists():
        return pd.read_csv(path)
    return pd.DataFrame()


def _write_csv(name: str, df: pd.DataFrame, data_dir: Optional[Path] = None) -> None:
    """Write a DataFrame to CSV."""
    path = _csv_path(name, data_dir)
    df.to_csv(path, index=False)


def _get_next_id(name: str, data_dir: Optional[Path] = None) -> int:
    """Get next ID for a table."""
    df = _read_csv(name, data_dir)
    if df.empty or "id" not in df.columns:
        return 1
    return int(df["id"].max()) + 1 if not df["id"].isna().all() else 1


# =============================================================================
# Bank Operations
# =============================================================================

def upsert_bank(code: str, name: str, data_dir: Optional[Path] = None) -> None:
    """Insert or update a bank."""
    df = _read_csv("banks", data_dir)

    if df.empty:
        df = pd.DataFrame([{"code": code, "name": name}])
    elif code in df["code"].values:
        df.loc[df["code"] == code, "name"] = name
    else:
        df = pd.concat([df, pd.DataFrame([{"code": code, "name": name}])], ignore_index=True)

    _write_csv("banks", df, data_dir)


def get_banks(data_dir: Optional[Path] = None) -> pd.DataFrame:
    """Get all banks."""
    df = _read_csv("banks", data_dir)
    if df.empty:
        return pd.DataFrame(columns=["code", "name"])
    return df.sort_values("code")


# =============================================================================
# Security Operations
# =============================================================================

def upsert_security(
    isin: str,
    name: Optional[str] = None,
    cusip: Optional[str] = None,
    issuer: Optional[str] = None,
    security_type: Optional[str] = None,
    payment_rank: Optional[str] = None,
    coupon_rate: Optional[float] = None,
    maturity_date: Optional[date] = None,
    currency: Optional[str] = None,
    rating_sp: Optional[str] = None,
    rating_moody: Optional[str] = None,
    modified_duration: Optional[float] = None,
    yield_to_maturity: Optional[float] = None,
    issuer_country: Optional[str] = None,
    issuer_sector: Optional[str] = None,
    data_dir: Optional[Path] = None
) -> None:
    """Insert or update a security."""
    df = _read_csv("securities", data_dir)

    new_data = {
        "isin": isin,
        "cusip": cusip,
        "name": name,
        "issuer": issuer,
        "security_type": security_type,
        "payment_rank": payment_rank,
        "coupon_rate": coupon_rate,
        "maturity_date": str(maturity_date) if maturity_date else None,
        "currency": currency,
        "rating_sp": rating_sp,
        "rating_moody": rating_moody,
        "modified_duration": modified_duration,
        "yield_to_maturity": yield_to_maturity,
        "issuer_country": issuer_country,
        "issuer_sector": issuer_sector,
        "last_enriched": None
    }

    if df.empty:
        df = pd.DataFrame([new_data])
    elif isin in df["isin"].values:
        # Update only non-null fields
        idx = df[df["isin"] == isin].index[0]
        for key, value in new_data.items():
            if value is not None and key != "isin":
                df.at[idx, key] = value
    else:
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

    _write_csv("securities", df, data_dir)


def get_securities(data_dir: Optional[Path] = None) -> pd.DataFrame:
    """Get all securities."""
    df = _read_csv("securities", data_dir)
    if df.empty:
        return pd.DataFrame(columns=[
            "isin", "cusip", "name", "issuer", "security_type", "payment_rank",
            "coupon_rate", "maturity_date", "currency", "rating_sp", "rating_moody",
            "modified_duration", "yield_to_maturity", "issuer_country", "issuer_sector",
            "last_enriched"
        ])
    return df.sort_values("isin")


def get_securities_needing_enrichment(data_dir: Optional[Path] = None) -> pd.DataFrame:
    """Get securities that haven't been enriched or need refresh."""
    df = _read_csv("securities", data_dir)
    if df.empty:
        return pd.DataFrame(columns=["isin", "name", "issuer", "currency"])

    mask = (
        df["last_enriched"].isna() |
        df["security_type"].isna() |
        df["payment_rank"].isna()
    )
    return df.loc[mask, ["isin", "name", "issuer", "currency"]].sort_values("isin")


def mark_securities_enriched(isins: list[str], data_dir: Optional[Path] = None) -> None:
    """Mark securities as enriched."""
    df = _read_csv("securities", data_dir)
    if df.empty:
        return

    today = str(date.today())
    for isin in isins:
        if isin in df["isin"].values:
            df.loc[df["isin"] == isin, "last_enriched"] = today

    _write_csv("securities", df, data_dir)


# =============================================================================
# Position Operations
# =============================================================================

def insert_position(
    bank_code: str,
    isin: str,
    statement_date: date,
    face_value: float,
    market_value: float,
    currency: str,
    source_file: str,
    market_price: Optional[float] = None,
    market_value_usd: Optional[float] = None,
    data_dir: Optional[Path] = None
) -> int:
    """Insert a new position. Returns the position ID."""
    df = _read_csv("positions", data_dir)
    position_id = _get_next_id("positions", data_dir)

    new_row = {
        "id": position_id,
        "bank_code": bank_code,
        "isin": isin,
        "statement_date": str(statement_date),
        "face_value": face_value,
        "market_price": market_price,
        "market_value": market_value,
        "market_value_usd": market_value_usd,
        "currency": currency,
        "source_file": source_file,
        "created_at": datetime.now().isoformat()
    }

    if df.empty:
        df = pd.DataFrame([new_row])
    else:
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    _write_csv("positions", df, data_dir)
    return position_id


def get_positions(
    statement_date: Optional[date] = None,
    bank_code: Optional[str] = None,
    data_dir: Optional[Path] = None
) -> pd.DataFrame:
    """Get positions with optional filters, joined with securities and banks."""
    positions_df = _read_csv("positions", data_dir)
    securities_df = _read_csv("securities", data_dir)
    banks_df = _read_csv("banks", data_dir)

    if positions_df.empty:
        return pd.DataFrame()

    # Apply filters
    if statement_date:
        positions_df = positions_df[positions_df["statement_date"] == str(statement_date)]
    if bank_code:
        positions_df = positions_df[positions_df["bank_code"] == bank_code]

    # Join with securities
    if not securities_df.empty:
        securities_cols = securities_df.rename(columns={
            "name": "security_name",
            "maturity_date": "security_maturity"
        })
        positions_df = positions_df.merge(
            securities_cols[["isin", "security_name", "issuer", "security_type", "payment_rank",
                           "coupon_rate", "security_maturity", "rating_sp", "rating_moody",
                           "modified_duration", "yield_to_maturity", "issuer_country", "issuer_sector"]],
            on="isin", how="left"
        )

    # Join with banks
    if not banks_df.empty:
        banks_cols = banks_df.rename(columns={"name": "bank_name"})
        positions_df = positions_df.merge(
            banks_cols[["code", "bank_name"]],
            left_on="bank_code", right_on="code", how="left"
        ).drop(columns=["code"], errors="ignore")

    return positions_df.sort_values(["bank_code", "issuer", "isin"] if "issuer" in positions_df.columns else ["bank_code", "isin"])


def get_latest_positions(data_dir: Optional[Path] = None) -> pd.DataFrame:
    """Get the most recent positions for each bank."""
    positions_df = _read_csv("positions", data_dir)

    if positions_df.empty:
        return pd.DataFrame()

    # Get max statement_date per bank
    latest_dates = positions_df.groupby("bank_code")["statement_date"].max().reset_index()
    latest_dates.columns = ["bank_code", "max_date"]

    # Filter to only latest positions
    positions_df = positions_df.merge(latest_dates, on="bank_code")
    positions_df = positions_df[positions_df["statement_date"] == positions_df["max_date"]]
    positions_df = positions_df.drop(columns=["max_date"])

    # Join with securities and banks
    securities_df = _read_csv("securities", data_dir)
    banks_df = _read_csv("banks", data_dir)

    if not securities_df.empty:
        securities_cols = securities_df.rename(columns={
            "name": "security_name",
            "maturity_date": "security_maturity"
        })
        positions_df = positions_df.merge(
            securities_cols[["isin", "security_name", "issuer", "security_type", "payment_rank",
                           "coupon_rate", "security_maturity", "rating_sp", "rating_moody",
                           "modified_duration", "yield_to_maturity", "issuer_country", "issuer_sector"]],
            on="isin", how="left"
        )

    if not banks_df.empty:
        banks_cols = banks_df.rename(columns={"name": "bank_name"})
        positions_df = positions_df.merge(
            banks_cols[["code", "bank_name"]],
            left_on="bank_code", right_on="code", how="left"
        ).drop(columns=["code"], errors="ignore")

    return positions_df.sort_values(["bank_code", "issuer", "isin"] if "issuer" in positions_df.columns else ["bank_code", "isin"])


def delete_positions_for_statement(
    bank_code: str,
    statement_date: date,
    data_dir: Optional[Path] = None
) -> int:
    """Delete positions for a specific statement. Returns count deleted."""
    df = _read_csv("positions", data_dir)
    if df.empty:
        return 0

    mask = (df["bank_code"] == bank_code) & (df["statement_date"] == str(statement_date))
    count = mask.sum()
    df = df[~mask]
    _write_csv("positions", df, data_dir)
    return count


# =============================================================================
# FX Rate Operations
# =============================================================================

def upsert_fx_rate(
    currency: str,
    rate_date: date,
    usd_rate: float,
    data_dir: Optional[Path] = None
) -> None:
    """Insert or update an FX rate (1 currency = X USD)."""
    df = _read_csv("fx_rates", data_dir)
    rate_date_str = str(rate_date)

    new_row = {"currency": currency, "rate_date": rate_date_str, "usd_rate": usd_rate}

    if df.empty:
        df = pd.DataFrame([new_row])
    else:
        mask = (df["currency"] == currency) & (df["rate_date"] == rate_date_str)
        if mask.any():
            df.loc[mask, "usd_rate"] = usd_rate
        else:
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    _write_csv("fx_rates", df, data_dir)


def get_fx_rate(
    currency: str,
    rate_date: date,
    data_dir: Optional[Path] = None
) -> Optional[float]:
    """Get FX rate for a currency on a specific date (or most recent before)."""
    if currency == "USD":
        return 1.0

    df = _read_csv("fx_rates", data_dir)
    if df.empty:
        return None

    # Filter by currency and date <= rate_date
    mask = (df["currency"] == currency) & (df["rate_date"] <= str(rate_date))
    filtered = df[mask].sort_values("rate_date", ascending=False)

    if filtered.empty:
        return None

    return float(filtered.iloc[0]["usd_rate"])


def get_all_fx_rates(data_dir: Optional[Path] = None) -> pd.DataFrame:
    """Get all FX rates."""
    df = _read_csv("fx_rates", data_dir)
    if df.empty:
        return pd.DataFrame(columns=["currency", "rate_date", "usd_rate"])
    return df.sort_values(["rate_date", "currency"], ascending=[False, True])


def import_fx_rates_from_csv(csv_path: Path, data_dir: Optional[Path] = None) -> int:
    """Import FX rates from external CSV. Returns count imported."""
    import_df = pd.read_csv(csv_path)
    count = 0

    for _, row in import_df.iterrows():
        upsert_fx_rate(
            currency=row["currency"],
            rate_date=pd.to_datetime(row["rate_date"]).date(),
            usd_rate=float(row["usd_rate"]),
            data_dir=data_dir
        )
        count += 1

    return count


# =============================================================================
# Statement Import Tracking
# =============================================================================

def record_import(
    bank_code: str,
    filename: str,
    statement_date: date,
    status: str,
    positions_extracted: int = 0,
    error_message: Optional[str] = None,
    data_dir: Optional[Path] = None
) -> int:
    """Record a statement import. Returns import ID."""
    df = _read_csv("imports", data_dir)
    import_id = _get_next_id("imports", data_dir)

    new_row = {
        "id": import_id,
        "bank_code": bank_code,
        "filename": filename,
        "statement_date": str(statement_date),
        "status": status,
        "positions_extracted": positions_extracted,
        "error_message": error_message,
        "processed_at": datetime.now().isoformat(),
        "created_at": datetime.now().isoformat()
    }

    if df.empty:
        df = pd.DataFrame([new_row])
    else:
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    _write_csv("imports", df, data_dir)
    return import_id


def get_imports(data_dir: Optional[Path] = None) -> pd.DataFrame:
    """Get all statement imports."""
    df = _read_csv("imports", data_dir)
    if df.empty:
        return pd.DataFrame(columns=[
            "id", "bank_code", "filename", "statement_date", "status",
            "positions_extracted", "error_message", "processed_at", "created_at"
        ])
    return df.sort_values("created_at", ascending=False)


# =============================================================================
# Utility Functions
# =============================================================================

def convert_positions_to_usd(
    statement_date: date,
    data_dir: Optional[Path] = None
) -> int:
    """Convert all position market values to USD. Returns count updated."""
    df = _read_csv("positions", data_dir)
    if df.empty:
        return 0

    count = 0
    statement_date_str = str(statement_date)

    for idx, row in df.iterrows():
        if row["statement_date"] != statement_date_str:
            continue
        if pd.notna(row.get("market_value_usd")):
            continue

        currency = row["currency"]
        market_value = row["market_value"]

        if currency == "USD":
            df.at[idx, "market_value_usd"] = market_value
            count += 1
        else:
            fx_rate = get_fx_rate(currency, statement_date, data_dir)
            if fx_rate:
                df.at[idx, "market_value_usd"] = market_value * fx_rate
                count += 1

    _write_csv("positions", df, data_dir)
    return count


def get_portfolio_summary(data_dir: Optional[Path] = None) -> dict:
    """Get a summary of the portfolio."""
    positions_df = get_latest_positions(data_dir)
    securities_df = _read_csv("securities", data_dir)

    summary = {}

    if positions_df.empty:
        summary["position_count"] = 0
        summary["security_count"] = 0
        summary["bank_count"] = 0
        summary["total_value_usd"] = 0
        summary["by_security_type"] = []
        return summary

    summary["position_count"] = len(positions_df)
    summary["security_count"] = positions_df["isin"].nunique()
    summary["bank_count"] = positions_df["bank_code"].nunique()
    summary["total_value_usd"] = positions_df["market_value_usd"].sum() if "market_value_usd" in positions_df.columns else None

    # By security type
    if "security_type" in positions_df.columns:
        type_breakdown = positions_df.groupby(positions_df["security_type"].fillna("Unknown")).agg({
            "isin": "count",
            "market_value_usd": "sum"
        }).reset_index()
        type_breakdown.columns = ["security_type", "count", "value_usd"]
        summary["by_security_type"] = type_breakdown.sort_values("value_usd", ascending=False).to_dict("records")
    else:
        summary["by_security_type"] = []

    return summary


# Backward compatibility aliases (for code that uses db_path parameter)
def _translate_path(db_path: Optional[Path] = None) -> Optional[Path]:
    """Translate old db_path to data_dir."""
    if db_path is None:
        return None
    # If it's a .duckdb file, use its parent directory
    if db_path.suffix == ".duckdb":
        return db_path.parent
    return db_path


if __name__ == "__main__":
    # Initialize CSV files when run directly
    print("Initializing CSV database...")
    init_database()
    print(f"CSV files created in: {DEFAULT_DATA_DIR}")
