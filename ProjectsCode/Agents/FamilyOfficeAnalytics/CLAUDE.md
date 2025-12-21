# FamilyOfficeAnalytics Agent

Extract fixed income positions from private bank PDF statements, consolidate across custodians, and generate analytics reports.

## Purpose

This agent processes scanned bank statements (PDFs) to:
1. Extract position data (ISIN, face value, market value, currency)
2. Store in DuckDB for analysis
3. Enrich via Bloomberg Terminal (manual Excel workflow)
4. Generate consolidation and concentration risk reports
5. Export for Bloomberg PORT upload

## Usage

```bash
cd /Users/vic-gini/ProjectsCode/Agents/FamilyOfficeAnalytics

# Process a single PDF
python -m src.main process input/statement.pdf --bank UBS

# Process all PDFs in input folder
python -m src.main process-all

# Generate Bloomberg enrichment request
python -m src.main enrich-request --output output/bloomberg_request.xlsx

# Import enriched data from Bloomberg
python -m src.main enrich-import output/bloomberg_enriched.xlsx

# Update FX rates
python -m src.main fx-update --file data/fx_rates.csv

# Generate reports
python -m src.main report consolidation --output output/consolidation.xlsx
python -m src.main report concentration --output output/concentration.xlsx

# Export for Bloomberg PORT
python -m src.main export port --output output/port_upload.csv
```

## Folder Structure

```
input/          # Drop bank statement PDFs here
output/         # Generated reports appear here
data/           # DuckDB database and FX rates
templates/      # Excel templates for Bloomberg workflow
```

## Monthly Workflow

1. Save bank statement PDFs to `input/`
2. Run `python -m src.main process-all`
3. Review any extraction errors
4. Run `python -m src.main enrich-request`
5. Open output Excel in Bloomberg Terminal, let BDP formulas populate, save
6. Run `python -m src.main enrich-import <file>`
7. Update FX rates if needed
8. Generate reports

## Configuration

Create `.env` file with:
```
ANTHROPIC_API_KEY=your_key_here
AWS_ACCESS_KEY_ID=your_key_here
AWS_SECRET_ACCESS_KEY=your_secret_here
AWS_REGION=ap-southeast-1
```

## Key Analytics

- **Consolidation**: All positions across banks with USD conversion
- **Concentration Risk**: Exposure by issuer, country, security type
- **Segmentation**: AT1, Tier 2, Subordinated debt breakdown
- **PORT Export**: Bloomberg-compatible format for portfolio upload

## Database

Uses DuckDB (local file at `data/portfolio.duckdb`). Schema:
- `banks` - Custodian information
- `securities` - Security master with Bloomberg enrichment
- `positions` - Point-in-time holdings
- `fx_rates` - Currency conversion rates
