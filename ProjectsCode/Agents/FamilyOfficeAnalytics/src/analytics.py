"""Portfolio analytics - consolidation and concentration risk analysis."""

import pandas as pd
from pathlib import Path
from typing import Optional
from dataclasses import dataclass
from datetime import date

from .database import get_latest_positions, get_connection


# Concentration risk thresholds
CONCENTRATION_THRESHOLDS = {
    "issuer": {"warning": 0.05, "critical": 0.10},
    "country": {"warning": 0.20, "critical": 0.30},
    "at1": {"warning": 0.10, "critical": 0.15},
    "subordinated": {"warning": 0.25, "critical": 0.35},
    "rating_bucket": {"warning": 0.30, "critical": 0.40},
    "currency": {"warning": 0.20, "critical": 0.30},
}


@dataclass
class ConcentrationAlert:
    """A concentration risk alert."""
    category: str  # issuer, country, security_type, etc.
    name: str  # The specific issuer/country/type
    exposure_usd: float
    exposure_pct: float
    threshold_type: str  # warning or critical
    threshold_value: float


def get_consolidated_positions(db_path: Optional[Path] = None) -> pd.DataFrame:
    """Get consolidated positions across all banks."""
    positions = get_latest_positions(db_path)

    if positions.empty:
        return positions

    # Add calculated fields
    positions["exposure_pct"] = (
        positions["market_value_usd"] / positions["market_value_usd"].sum() * 100
    )

    return positions


def get_portfolio_summary(db_path: Optional[Path] = None) -> dict:
    """Get high-level portfolio summary."""
    positions = get_consolidated_positions(db_path)

    if positions.empty:
        return {
            "total_positions": 0,
            "total_value_usd": 0,
            "unique_securities": 0,
            "bank_count": 0,
        }

    return {
        "total_positions": len(positions),
        "total_value_usd": positions["market_value_usd"].sum(),
        "unique_securities": positions["isin"].nunique(),
        "bank_count": positions["bank_code"].nunique(),
        "currencies": positions["currency"].unique().tolist(),
        "statement_dates": positions.groupby("bank_code")["statement_date"].first().to_dict(),
    }


def get_segmentation_by_security_type(db_path: Optional[Path] = None) -> pd.DataFrame:
    """
    Get portfolio breakdown by security type.

    Returns breakdown of AT1, Tier2, Subordinated, Senior, etc.
    """
    positions = get_consolidated_positions(db_path)

    if positions.empty:
        return pd.DataFrame()

    total_value = positions["market_value_usd"].sum()

    segmentation = positions.groupby("security_type").agg({
        "isin": "count",
        "market_value_usd": "sum",
        "modified_duration": "mean",
        "yield_to_maturity": "mean",
    }).reset_index()

    segmentation.columns = ["security_type", "position_count", "value_usd", "avg_duration", "avg_ytm"]
    segmentation["pct_of_portfolio"] = segmentation["value_usd"] / total_value * 100
    segmentation = segmentation.sort_values("value_usd", ascending=False)

    return segmentation


def get_segmentation_by_payment_rank(db_path: Optional[Path] = None) -> pd.DataFrame:
    """Get portfolio breakdown by payment rank (seniority)."""
    positions = get_consolidated_positions(db_path)

    if positions.empty:
        return pd.DataFrame()

    total_value = positions["market_value_usd"].sum()

    segmentation = positions.groupby("payment_rank").agg({
        "isin": "count",
        "market_value_usd": "sum",
        "modified_duration": "mean",
        "yield_to_maturity": "mean",
    }).reset_index()

    segmentation.columns = ["payment_rank", "position_count", "value_usd", "avg_duration", "avg_ytm"]
    segmentation["pct_of_portfolio"] = segmentation["value_usd"] / total_value * 100
    segmentation = segmentation.sort_values("value_usd", ascending=False)

    return segmentation


def get_concentration_by_issuer(db_path: Optional[Path] = None) -> pd.DataFrame:
    """Get concentration by issuer."""
    positions = get_consolidated_positions(db_path)

    if positions.empty:
        return pd.DataFrame()

    total_value = positions["market_value_usd"].sum()

    concentration = positions.groupby(["issuer", "issuer_country"]).agg({
        "isin": "nunique",
        "market_value_usd": "sum",
    }).reset_index()

    concentration.columns = ["issuer", "country", "security_count", "value_usd"]
    concentration["pct_of_portfolio"] = concentration["value_usd"] / total_value * 100
    concentration = concentration.sort_values("value_usd", ascending=False)

    return concentration


def get_concentration_by_country(db_path: Optional[Path] = None) -> pd.DataFrame:
    """Get concentration by country."""
    positions = get_consolidated_positions(db_path)

    if positions.empty:
        return pd.DataFrame()

    total_value = positions["market_value_usd"].sum()

    concentration = positions.groupby("issuer_country").agg({
        "isin": "nunique",
        "issuer": "nunique",
        "market_value_usd": "sum",
    }).reset_index()

    concentration.columns = ["country", "security_count", "issuer_count", "value_usd"]
    concentration["pct_of_portfolio"] = concentration["value_usd"] / total_value * 100
    concentration = concentration.sort_values("value_usd", ascending=False)

    return concentration


def get_concentration_by_rating(db_path: Optional[Path] = None) -> pd.DataFrame:
    """Get concentration by credit rating."""
    positions = get_consolidated_positions(db_path)

    if positions.empty:
        return pd.DataFrame()

    total_value = positions["market_value_usd"].sum()

    # Use S&P rating, fall back to Moody's
    positions["rating"] = positions["rating_sp"].fillna(positions["rating_moody"])

    # Create rating buckets
    def rating_bucket(rating):
        if pd.isna(rating):
            return "Not Rated"
        rating = str(rating).upper()
        if any(r in rating for r in ["AAA", "AA"]):
            return "AA and above"
        if "A" in rating and "B" not in rating:
            return "A"
        if "BBB" in rating or "BAA" in rating:
            return "BBB"
        if "BB" in rating or "BA" in rating:
            return "BB"
        if "B" in rating and "BB" not in rating:
            return "B and below"
        return "Other"

    positions["rating_bucket"] = positions["rating"].apply(rating_bucket)

    concentration = positions.groupby("rating_bucket").agg({
        "isin": "nunique",
        "market_value_usd": "sum",
    }).reset_index()

    concentration.columns = ["rating_bucket", "security_count", "value_usd"]
    concentration["pct_of_portfolio"] = concentration["value_usd"] / total_value * 100

    # Sort by rating quality
    rating_order = ["AA and above", "A", "BBB", "BB", "B and below", "Not Rated", "Other"]
    concentration["sort_order"] = concentration["rating_bucket"].apply(
        lambda x: rating_order.index(x) if x in rating_order else 99
    )
    concentration = concentration.sort_values("sort_order").drop(columns=["sort_order"])

    return concentration


def get_concentration_by_currency(db_path: Optional[Path] = None) -> pd.DataFrame:
    """Get concentration by currency."""
    positions = get_consolidated_positions(db_path)

    if positions.empty:
        return pd.DataFrame()

    total_value = positions["market_value_usd"].sum()

    concentration = positions.groupby("currency").agg({
        "isin": "nunique",
        "market_value_usd": "sum",
    }).reset_index()

    concentration.columns = ["currency", "security_count", "value_usd"]
    concentration["pct_of_portfolio"] = concentration["value_usd"] / total_value * 100
    concentration = concentration.sort_values("value_usd", ascending=False)

    return concentration


def get_concentration_by_maturity(db_path: Optional[Path] = None) -> pd.DataFrame:
    """Get concentration by maturity bucket."""
    positions = get_consolidated_positions(db_path)

    if positions.empty:
        return pd.DataFrame()

    total_value = positions["market_value_usd"].sum()

    # Create maturity buckets
    today = pd.Timestamp.today()

    def maturity_bucket(mat_date):
        if pd.isna(mat_date):
            return "Perpetual/Unknown"
        mat_date = pd.Timestamp(mat_date)
        years = (mat_date - today).days / 365.25
        if years <= 1:
            return "0-1 Year"
        elif years <= 3:
            return "1-3 Years"
        elif years <= 5:
            return "3-5 Years"
        elif years <= 10:
            return "5-10 Years"
        else:
            return "10+ Years"

    positions["maturity_bucket"] = positions["security_maturity"].apply(maturity_bucket)

    concentration = positions.groupby("maturity_bucket").agg({
        "isin": "nunique",
        "market_value_usd": "sum",
        "modified_duration": "mean",
    }).reset_index()

    concentration.columns = ["maturity_bucket", "security_count", "value_usd", "avg_duration"]
    concentration["pct_of_portfolio"] = concentration["value_usd"] / total_value * 100

    # Sort by maturity
    bucket_order = ["0-1 Year", "1-3 Years", "3-5 Years", "5-10 Years", "10+ Years", "Perpetual/Unknown"]
    concentration["sort_order"] = concentration["maturity_bucket"].apply(
        lambda x: bucket_order.index(x) if x in bucket_order else 99
    )
    concentration = concentration.sort_values("sort_order").drop(columns=["sort_order"])

    return concentration


def check_concentration_alerts(
    db_path: Optional[Path] = None,
    thresholds: Optional[dict] = None
) -> list[ConcentrationAlert]:
    """
    Check for concentration risk alerts.

    Returns list of ConcentrationAlert objects for any threshold breaches.
    """
    thresholds = thresholds or CONCENTRATION_THRESHOLDS
    alerts = []

    # Issuer concentration
    issuer_conc = get_concentration_by_issuer(db_path)
    for _, row in issuer_conc.iterrows():
        pct = row["pct_of_portfolio"] / 100
        if pct >= thresholds["issuer"]["critical"]:
            alerts.append(ConcentrationAlert(
                category="issuer",
                name=row["issuer"],
                exposure_usd=row["value_usd"],
                exposure_pct=row["pct_of_portfolio"],
                threshold_type="critical",
                threshold_value=thresholds["issuer"]["critical"] * 100
            ))
        elif pct >= thresholds["issuer"]["warning"]:
            alerts.append(ConcentrationAlert(
                category="issuer",
                name=row["issuer"],
                exposure_usd=row["value_usd"],
                exposure_pct=row["pct_of_portfolio"],
                threshold_type="warning",
                threshold_value=thresholds["issuer"]["warning"] * 100
            ))

    # Country concentration
    country_conc = get_concentration_by_country(db_path)
    for _, row in country_conc.iterrows():
        pct = row["pct_of_portfolio"] / 100
        if pct >= thresholds["country"]["critical"]:
            alerts.append(ConcentrationAlert(
                category="country",
                name=row["country"],
                exposure_usd=row["value_usd"],
                exposure_pct=row["pct_of_portfolio"],
                threshold_type="critical",
                threshold_value=thresholds["country"]["critical"] * 100
            ))
        elif pct >= thresholds["country"]["warning"]:
            alerts.append(ConcentrationAlert(
                category="country",
                name=row["country"],
                exposure_usd=row["value_usd"],
                exposure_pct=row["pct_of_portfolio"],
                threshold_type="warning",
                threshold_value=thresholds["country"]["warning"] * 100
            ))

    # AT1 concentration
    type_conc = get_segmentation_by_security_type(db_path)
    at1_row = type_conc[type_conc["security_type"] == "AT1"]
    if not at1_row.empty:
        pct = at1_row.iloc[0]["pct_of_portfolio"] / 100
        if pct >= thresholds["at1"]["critical"]:
            alerts.append(ConcentrationAlert(
                category="security_type",
                name="AT1",
                exposure_usd=at1_row.iloc[0]["value_usd"],
                exposure_pct=at1_row.iloc[0]["pct_of_portfolio"],
                threshold_type="critical",
                threshold_value=thresholds["at1"]["critical"] * 100
            ))
        elif pct >= thresholds["at1"]["warning"]:
            alerts.append(ConcentrationAlert(
                category="security_type",
                name="AT1",
                exposure_usd=at1_row.iloc[0]["value_usd"],
                exposure_pct=at1_row.iloc[0]["pct_of_portfolio"],
                threshold_type="warning",
                threshold_value=thresholds["at1"]["warning"] * 100
            ))

    # Subordinated debt concentration (AT1 + Tier2 + Subordinated)
    sub_types = ["AT1", "TIER2", "SUBORDINATED"]
    sub_rows = type_conc[type_conc["security_type"].isin(sub_types)]
    if not sub_rows.empty:
        total_sub_pct = sub_rows["pct_of_portfolio"].sum() / 100
        total_sub_usd = sub_rows["value_usd"].sum()
        if total_sub_pct >= thresholds["subordinated"]["critical"]:
            alerts.append(ConcentrationAlert(
                category="subordinated_total",
                name="All Subordinated Debt",
                exposure_usd=total_sub_usd,
                exposure_pct=total_sub_pct * 100,
                threshold_type="critical",
                threshold_value=thresholds["subordinated"]["critical"] * 100
            ))
        elif total_sub_pct >= thresholds["subordinated"]["warning"]:
            alerts.append(ConcentrationAlert(
                category="subordinated_total",
                name="All Subordinated Debt",
                exposure_usd=total_sub_usd,
                exposure_pct=total_sub_pct * 100,
                threshold_type="warning",
                threshold_value=thresholds["subordinated"]["warning"] * 100
            ))

    # Non-USD currency concentration
    currency_conc = get_concentration_by_currency(db_path)
    non_usd = currency_conc[currency_conc["currency"] != "USD"]
    for _, row in non_usd.iterrows():
        pct = row["pct_of_portfolio"] / 100
        if pct >= thresholds["currency"]["critical"]:
            alerts.append(ConcentrationAlert(
                category="currency",
                name=row["currency"],
                exposure_usd=row["value_usd"],
                exposure_pct=row["pct_of_portfolio"],
                threshold_type="critical",
                threshold_value=thresholds["currency"]["critical"] * 100
            ))
        elif pct >= thresholds["currency"]["warning"]:
            alerts.append(ConcentrationAlert(
                category="currency",
                name=row["currency"],
                exposure_usd=row["value_usd"],
                exposure_pct=row["pct_of_portfolio"],
                threshold_type="warning",
                threshold_value=thresholds["currency"]["warning"] * 100
            ))

    return alerts


def get_duplicate_holdings(db_path: Optional[Path] = None) -> pd.DataFrame:
    """Find securities held at multiple banks."""
    positions = get_consolidated_positions(db_path)

    if positions.empty:
        return pd.DataFrame()

    # Group by ISIN and count banks
    duplicates = positions.groupby("isin").agg({
        "bank_code": lambda x: list(x.unique()),
        "security_name": "first",
        "issuer": "first",
        "market_value_usd": "sum",
    }).reset_index()

    duplicates["bank_count"] = duplicates["bank_code"].apply(len)
    duplicates = duplicates[duplicates["bank_count"] > 1]
    duplicates = duplicates.sort_values("market_value_usd", ascending=False)

    return duplicates


if __name__ == "__main__":
    print("Portfolio Analytics")
    print("=" * 50)

    summary = get_portfolio_summary()
    print(f"\nPortfolio Summary:")
    print(f"  Total Positions: {summary['total_positions']}")
    print(f"  Total Value (USD): ${summary['total_value_usd']:,.2f}" if summary['total_value_usd'] else "  No data")

    print("\nSecurity Type Breakdown:")
    seg = get_segmentation_by_security_type()
    if not seg.empty:
        for _, row in seg.iterrows():
            print(f"  {row['security_type']}: {row['pct_of_portfolio']:.1f}%")

    print("\nConcentration Alerts:")
    alerts = check_concentration_alerts()
    if alerts:
        for alert in alerts:
            print(f"  [{alert.threshold_type.upper()}] {alert.category}: {alert.name} ({alert.exposure_pct:.1f}%)")
    else:
        print("  No concentration alerts")
