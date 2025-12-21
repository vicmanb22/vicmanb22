# FamilyOfficeAnalytics Project

Portfolio analytics system for a family office with fixed income holdings across multiple private banks.

## Overview

This project extracts position data from scanned bank statement PDFs, consolidates across 6 custodians (~400 positions), enriches via Bloomberg Terminal, and produces analytics reports.

## Components

- **Agent**: `/Users/vic-gini/ProjectsCode/Agents/FamilyOfficeAnalytics/` - The processing tool
- **Project**: This directory - Documentation and archived statements

## Current Status

**V1 (POC)** - In Development
- Local DuckDB database
- AWS Textract for OCR
- Claude for intelligent parsing
- Excel reports
- Bloomberg enrichment via Excel Add-in

## Analytics Produced

### Consolidation Report
- All positions across banks
- USD-converted market values
- Grouped by bank, security type, issuer

### Concentration Risk Report
- Single issuer exposure (warning >5%, critical >10%)
- Country concentration (warning >20%, critical >30%)
- AT1 exposure (warning >10%, critical >15%)
- Subordinated debt total (warning >25%, critical >35%)
- Rating bucket concentration
- Currency exposure (non-USD)

### Segmentation
- AT1 bonds
- Tier 2 capital instruments
- Subordinated debt
- Senior debt

## Monthly Workflow

See `docs/workflow.md` for the complete monthly processing guide.

## Future (V2)

- PostgreSQL on AWS Singapore
- Multi-user access
- Web dashboard
- Automated processing
