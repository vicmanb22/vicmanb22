# Master Folder Hierarchy

## Primary Structure

This folder hierarchy should be consistent across all cloud drives and local storage.

```
Documents/
├── Personal/
│   ├── Identity/                       # Passports, IDs, certificates
│   ├── Family/                         # Family-related documents
│   │   ├── Nara/                       # Nara-specific documents
│   │   └── General/                    # Family events, records
│   ├── Medical/                        # Health records, prescriptions
│   ├── Legal/                          # Personal legal documents
│   └── Correspondence/                 # Personal letters, cards
│
├── Work/
│   ├── VerifiedMetrics/                # VM company files
│   │   ├── Clients/
│   │   ├── Contracts/
│   │   ├── Invoices/
│   │   ├── Reports/
│   │   └── Projects/
│   ├── ArgonautExpeditions/            # Argonaut files
│   ├── IDEACIMUN/                      # IDEA/CIMUN files
│   └── CloudviewRealEstate/            # Cloudview files
│       ├── Properties/
│       ├── Tenants/
│       └── Financials/
│
├── Finance/
│   ├── Banking/                        # Bank statements, records
│   │   ├── Chase/
│   │   ├── [Other Banks]/
│   │   └── CreditCards/
│   ├── Taxes/                          # Tax returns, forms
│   │   ├── 2024/
│   │   ├── 2025/
│   │   └── Reference/                  # Tax guides, notes
│   ├── Investments/                    # Investment statements
│   ├── Insurance/                      # Policies, claims
│   └── Receipts/                       # Purchase receipts
│
├── Reference/
│   ├── Manuals/                        # Product manuals
│   ├── Guides/                         # How-to guides
│   ├── Research/                       # Research materials
│   └── Templates/                      # Reusable templates
│
└── Archive/                            # Historical/legacy files
    ├── Pre-2024/
    └── Legacy-Unsorted/

Pictures/
├── 2024/
│   ├── January/
│   ├── February/
│   └── .../
├── 2025/
│   └── .../
├── Family/                             # Family event photos
│   └── [Event Name]/
├── Work/                               # Work-related images
│   └── [Project Name]/
└── Screenshots/                        # Screen captures
    └── YYYY-MM/

ToDelete/                               # Deletion staging area
├── YYYY-MM/                            # Date-based folders
│   ├── VerifiedMetrics/
│   ├── ArgonautExpeditions/
│   ├── IDEACIMUN/
│   ├── CloudviewRealEstate/
│   ├── Family/
│   ├── PersonalFinance/
│   ├── Recovery/
│   ├── LifeAndFun/
│   ├── OrganizationRoutinesMaintenance/
│   ├── Reference/
│   └── Media/
└── permanent-delete-queue/             # 30+ day old, ready for deletion

NeedsReview/                            # Ambiguous files
└── YYYY-MM-DD/                         # Date flagged
```

## Cloud Drive Assignments

### iCloud Drive
**Primary use:** Personal files, Obsidian vault, iOS-synced content
**Path:** `/Users/vic-gini/Library/Mobile Documents/com~apple~CloudDocs/`

Recommended structure:
- Documents/ (mirror of main hierarchy)
- Downloads/ (iOS downloads, quick saves)
- Obsidian vault (EXCLUDED from FileOrganizer)

### Google Drive (Personal)
**Primary use:** Personal backup, sharing with family
**Path:** `/Users/vic-gini/victor.lang22@gmail.com - Google Drive/My Drive/`

Recommended structure:
- Documents/ (personal documents backup)
- Shared/ (files shared with family)
- Archive/ (long-term personal archive)

### Google Drive (Work)
**Primary use:** Verified Metrics business files
**Path:** `/Users/vic-gini/victor@verifiedmetrics.com - Google Drive/`

Recommended structure:
- Clients/
- Projects/
- Contracts/
- Finance/
- Team/ (shared with team members)

### Dropbox (Personal)
**Primary use:** Legacy personal files
**Path:** `/Users/vic-gini/Dropbox/`

May have older organization; good candidate for audit.

### Dropbox (Cloudview)
**Primary use:** Cloudview Real Estate shared files
**Path:** `/Users/vic-gini/Cloudview Dropbox/Victor Lang (Home)/`

Shared with Cloudview partners; follow their conventions where applicable.

### Local Documents
**Primary use:** Active working files, primary workspace
**Path:** `/Users/vic-gini/Documents/`

This is the canonical location for the full folder hierarchy.

### Local Downloads
**Primary use:** Incoming files (temporary)
**Path:** `/Users/vic-gini/Downloads/`

Should be triaged regularly; nothing should live here permanently.

### Local Desktop
**Primary use:** Quick access files (temporary)
**Path:** `/Users/vic-gini/Desktop/`

Should be triaged regularly; keep minimal.

## Category → Folder Mapping

| Category | Primary Folder |
|----------|----------------|
| VerifiedMetrics | Documents/Work/VerifiedMetrics/ |
| ArgonautExpeditions | Documents/Work/ArgonautExpeditions/ |
| IDEACIMUN | Documents/Work/IDEACIMUN/ |
| CloudviewRealEstate | Documents/Work/CloudviewRealEstate/ |
| Family | Documents/Personal/Family/ |
| PersonalFinance | Documents/Finance/ |
| Recovery | Documents/Personal/Medical/ |
| LifeAndFun | Documents/Personal/ |
| OrganizationRoutinesMaintenance | Documents/Personal/ |
| Reference | Documents/Reference/ |
| Media | Pictures/ or appropriate subfolder |
| Archive | Documents/Archive/ |

## Folder Creation Rules

1. **Create year folders as needed** (2024, 2025, etc.)
2. **Create entity subfolders** when 5+ files from same entity
3. **Use descriptive names** for project/event folders
4. **Avoid deep nesting** (max 4 levels preferred)
5. **Don't create empty folders** in advance
