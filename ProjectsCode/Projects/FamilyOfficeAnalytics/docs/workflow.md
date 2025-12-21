# FamilyOfficeAnalytics Monthly Workflow

## Prerequisites

1. AWS credentials configured (for Textract OCR)
2. Anthropic API key configured
3. Bloomberg Terminal access (for enrichment)

## Step-by-Step Process

### 1. Collect Bank Statements

Receive monthly PDF statements from each bank and save to:
```
/Users/vic-gini/ProjectsCode/Agents/FamilyOfficeAnalytics/input/
```

Naming convention: `{BANK}_{YYYY}_{MM}.pdf`
- Example: `UBS_2024_11.pdf`

### 2. Process PDFs

```bash
cd /Users/vic-gini/ProjectsCode/Agents/FamilyOfficeAnalytics
python -m src.main process-all
```

This will:
- OCR each PDF using AWS Textract
- Parse positions using Claude
- Store in DuckDB database

### 3. Review Extraction

Check the output for any extraction errors or warnings.
Manually review flagged positions if needed.

### 4. Generate Bloomberg Enrichment Request

```bash
python -m src.main enrich-request --output output/bloomberg_request.xlsx
```

This creates an Excel file with ISINs that need Bloomberg data.

### 5. Enrich in Bloomberg Terminal

1. Open `bloomberg_request.xlsx` in Excel on Bloomberg Terminal
2. The BDP formulas will auto-populate with:
   - Security type
   - Payment rank (AT1, Tier2, Senior, Sub)
   - Yield to maturity
   - Modified duration
   - Credit ratings (S&P, Moody's)
   - Country of risk
   - Industry sector
3. Wait for all formulas to calculate
4. Save as `bloomberg_enriched.xlsx`

### 6. Import Enrichment

```bash
python -m src.main enrich-import output/bloomberg_enriched.xlsx
```

### 7. Update FX Rates

Update `data/fx_rates.csv` with current rates, then:
```bash
python -m src.main fx-update --file data/fx_rates.csv
```

FX rates CSV format:
```csv
currency,rate_date,usd_rate
EUR,2024-11-30,1.0534
GBP,2024-11-30,1.2654
CHF,2024-11-30,0.8821
SGD,2024-11-30,0.7432
```

### 8. Generate Reports

```bash
# Consolidation report - all positions across banks
python -m src.main report consolidation --output output/consolidation.xlsx

# Concentration risk report
python -m src.main report concentration --output output/concentration.xlsx
```

### 9. Bloomberg PORT Upload (Optional)

```bash
python -m src.main export port --output output/port_upload.csv
```

In Bloomberg Terminal:
1. Type `PRTU` and press Enter
2. Select Import → CSV
3. Choose `port_upload.csv`
4. Map columns as prompted
5. Complete import

### 10. Archive Statements

Move processed PDFs to:
```
/Users/vic-gini/ProjectsCode/Projects/FamilyOfficeAnalytics/historical/{YYYY}/{MM}/
```

## Troubleshooting

### OCR Quality Issues
- Ensure PDFs are reasonably clear scans
- Very faded or skewed documents may need manual entry

### Missing ISINs
- Some older securities may not have ISINs
- Use CUSIP or manually add to securities table

### Bloomberg Enrichment Fails
- Check ISIN format (12 characters, starts with country code)
- Some securities may not be in Bloomberg
- Manual lookup may be required

## Report Delivery

Generated reports are saved to:
```
/Users/vic-gini/ProjectsCode/Agents/FamilyOfficeAnalytics/output/
```

Files:
- `consolidation.xlsx` - Full position listing
- `concentration.xlsx` - Risk analysis
- `port_upload.csv` - Bloomberg PORT format
