# Graph Report - .  (2026-04-21)

## Corpus Check
- Corpus is ~21,269 words - fits in a single context window. You may not need a graph.

## Summary
- 230 nodes · 392 edges · 32 communities detected
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 22 edges (avg confidence: 0.82)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Data Bootstrap & DB State|Data Bootstrap & DB State]]
- [[_COMMUNITY_Roles & Invite Flow|Roles & Invite Flow]]
- [[_COMMUNITY_App Init & Auth|App Init & Auth]]
- [[_COMMUNITY_Invoice & GST Engine|Invoice & GST Engine]]
- [[_COMMUNITY_Ageing Analysis & Client Forms|Ageing Analysis & Client Forms]]
- [[_COMMUNITY_Deep Dive Documentation|Deep Dive Documentation]]
- [[_COMMUNITY_Product Positioning|Product Positioning]]
- [[_COMMUNITY_Dashboard & Render Utils|Dashboard & Render Utils]]
- [[_COMMUNITY_Section Loaders|Section Loaders]]
- [[_COMMUNITY_Navigation & OCR Modal|Navigation & OCR Modal]]
- [[_COMMUNITY_OCR Processing|OCR Processing]]
- [[_COMMUNITY_Onboarding Wizard|Onboarding Wizard]]
- [[_COMMUNITY_Multi-Tenant Architecture|Multi-Tenant Architecture]]
- [[_COMMUNITY_Weekly Timesheet|Weekly Timesheet]]
- [[_COMMUNITY_Project & Time Sections|Project & Time Sections]]
- [[_COMMUNITY_Invoice Print Rendering|Invoice Print Rendering]]
- [[_COMMUNITY_Admin vs Client Roles|Admin vs Client Roles]]
- [[_COMMUNITY_Fast Onboarding|Fast Onboarding]]
- [[_COMMUNITY_Invite Link Flow|Invite Link Flow]]
- [[_COMMUNITY_Chart of Accounts|Chart of Accounts]]
- [[_COMMUNITY_Data Portability|Data Portability]]
- [[_COMMUNITY_Time Tracking Problem|Time Tracking Problem]]
- [[_COMMUNITY_Party Master|Party Master]]
- [[_COMMUNITY_Ageing Analysis Section|Ageing Analysis Section]]
- [[_COMMUNITY_Module Overview|Module Overview]]
- [[_COMMUNITY_Data Architecture|Data Architecture]]
- [[_COMMUNITY_Market Opportunity|Market Opportunity]]
- [[_COMMUNITY_Business Model|Business Model]]
- [[_COMMUNITY_Seed Ask|Seed Ask]]
- [[_COMMUNITY_Dashboard Section|Dashboard Section]]
- [[_COMMUNITY_Items Section|Items Section]]
- [[_COMMUNITY_Setup Section|Setup Section]]

## God Nodes (most connected - your core abstractions)
1. `loadAllData` - 23 edges
2. `toast()` - 20 edges
3. `openModal()` - 13 edges
4. `saveModal()` - 12 edges
5. `isAdmin()` - 11 edges
6. `fmt()` - 11 edges
7. `esc()` - 9 edges
8. `refreshInvoiceTypeOnPartyChange()` - 9 edges
9. `updateBadges()` - 8 edges
10. `determineInvoiceTypes()` - 8 edges

## Surprising Connections (you probably didn't know these)
- `loadAllData` --calls--> `toast()`  [EXTRACTED]
  graphify-in/kepei-app.js → graphify-in\kepei-app.js
- `saveModal` --calls--> `toast()`  [EXTRACTED]
  graphify-in/kepei-app.js → graphify-in\kepei-app.js
- `saveSetup` --calls--> `toast()`  [EXTRACTED]
  graphify-in/kepei-app.js → graphify-in\kepei-app.js
- `5-Step Onboarding Wizard` --semantically_similar_to--> `Solution: 60-Second Client Onboarding`  [INFERRED] [semantically similar]
  graphify-in/Kepei-CA-Admin-Guide.md → graphify-in/Kepei-Problems-Solutions.md
- `Solution: One Invoice = Three Auto-Records` --semantically_similar_to--> `One Invoice = Three Auto-Created Records`  [INFERRED] [semantically similar]
  graphify-in/Kepei-Problems-Solutions.md → graphify-in/Kepei-Deep-Dive.md

## Hyperedges (group relationships)
- **30 Problem-Solution Pairs (Core Product Rationale)** — problems_triple_data_entry, problems_solution_one_invoice_three, problems_gst_manual_error_prone, problems_solution_gst_engine, problems_multi_client_nightmare, problems_solution_multitenant [EXTRACTED 1.00]
- **loadAllData as sole writer for all DB subcollection fields** — kepei_app_loadAllData, kepei_app_DB_setup, kepei_app_DB_coa, kepei_app_DB_parties, kepei_app_DB_items, kepei_app_DB_invoices, kepei_app_sole_writer_contract [EXTRACTED 0.95]
- **App bootstrap: auth -> loadAllData -> render** — kepei_app_firebase_auth, kepei_app_doLogin, kepei_app_loadAllData, kepei_app_loadDashboard [EXTRACTED 0.90]
- **loadAllData try/catch + toast + re-throw error-handling pattern** — kepei_app_loadAllData, kepei_app_toast, kepei_app_fail_fast_rationale, kepei_app_firebase_firestore [EXTRACTED 0.95]
- **Three-version schema migration (single-doc -> split-doc -> subcollection)** — kepei_app_subcollection_migration, kepei_app_loadAllData, kepei_app_firebase_firestore, kepei_app_DEFAULT_COA [EXTRACTED 0.90]
- **Firestore CRUD family sharing DB state and collection path pattern** — kepei_app_addRecord, kepei_app_updateRecord, kepei_app_deleteRecord, kepei_app_saveCollection, kepei_app_saveAllData [INFERRED 0.85]

## Communities

### Community 0 - "Data Bootstrap & DB State"
Cohesion: 0.08
Nodes (36): DB.coa, DB.fixed_assets, DB.gst_ledger, DB.inventory, DB.invites, DB.invoices, DB.items, DB.parties (+28 more)

### Community 1 - "Roles & Invite Flow"
Cohesion: 0.11
Nodes (23): addRecord(), applyRole(), completeSignup(), copyInviteLink(), copyToClipboard(), deleteEntry(), deleteRecord(), exportData() (+15 more)

### Community 2 - "App Init & Auth"
Cohesion: 0.1
Nodes (2): startTimer(), stopTimer()

### Community 3 - "Invoice & GST Engine"
Cohesion: 0.16
Nodes (21): addInvoiceLine(), closeModal(), createUserAccount(), determineInvoiceTypes(), getBuyerGSTProfile(), getGSTRegime(), getInvoiceTypeOptions(), getLineItemHeaders() (+13 more)

### Community 4 - "Ageing Analysis & Client Forms"
Cohesion: 0.15
Nodes (19): applyOCRToClientForm(), calcAgeingData(), closeClientForm(), drillPartyAgeing(), esc(), exportAgeingData(), fmt(), loadAgeingAnalysis() (+11 more)

### Community 5 - "Deep Dive Documentation"
Cohesion: 0.14
Nodes (14): Fixed Assets & TDS Module, GST Engine: CGST/SGST/IGST Auto-Split, One Invoice = Three Auto-Created Records, Stock Register â€” Invoice-Driven Automation, Solution: One Invoice = Three Auto-Records, Problem: Triple Data Entry (Invoice+GST+Stock), Fixed Assets Section, GST Ledger Section (+6 more)

### Community 6 - "Product Positioning"
Cohesion: 0.18
Nodes (11): Dashboard Zero-Load Architecture, Feature Matrix vs Tally/Zoho/Vyapar, Firestore Subcollection Scalability, India-First GST Engine (Core Architecture), Zero Infrastructure â€” Single HTML File, Problem: 63M MSMEs Lack GST-Ready Software, Scale Roadmap (v3 â†’ API â†’ PWA â†’ White-label), Problem: Client Has No Book Visibility (+3 more)

### Community 7 - "Dashboard & Render Utils"
Cohesion: 0.27
Nodes (10): formatCurrency(), initApp(), loadDashboard(), renderClientBilling(), renderDetailedLog(), renderProfitability(), renderReport(), renderStaffUtil() (+2 more)

### Community 8 - "Section Loaders"
Cohesion: 0.22
Nodes (9): filterGST(), loadGSTLedger(), loadInventory(), loadInvoices(), loadItems(), loadParties(), loadTransactions(), toggleClientView() (+1 more)

### Community 9 - "Navigation & OCR Modal"
Cohesion: 0.22
Nodes (9): acceptOCRResult(), closeOCRModal(), navigate(), openOCRModal(), resetOCRModal(), showTut(), skipTutorial(), startTutorial() (+1 more)

### Community 10 - "OCR Processing"
Cohesion: 0.29
Nodes (7): displayOCRResult(), extractOCRFields(), handleOCRDrop(), handleOCRFile(), processOCRText(), runTesseractOCR(), setOCRProgress()

### Community 11 - "Onboarding Wizard"
Cohesion: 0.33
Nodes (7): genRecs(), initWizard(), showOnboarding(), showWizStep(), updateStepDots(), wizBack(), wizNext()

### Community 12 - "Multi-Tenant Architecture"
Cohesion: 0.4
Nodes (5): Multi-Tenant User Management Architecture, CA Firm as Distribution Channel, Problem: Managing Multiple Clients is Difficult, Solution: Multi-Tenant Architecture, User Management Section

### Community 13 - "Weekly Timesheet"
Cohesion: 0.5
Nodes (4): loadBulkEntry(), loadWeeklyTimesheet(), shiftWeek(), switchTimeTab()

### Community 14 - "Project & Time Sections"
Cohesion: 0.5
Nodes (4): Projects & Time Tracking (3 Entry Modes), Projects Section, Time Entries Section, Time Reports Section

### Community 15 - "Invoice Print Rendering"
Cohesion: 0.67
Nodes (3): generateInvoiceHTML(), numberToWords(), viewInvoice()

### Community 16 - "Admin vs Client Roles"
Cohesion: 0.67
Nodes (3): Admin vs Client Role Separation, Client-Visible Modules (8 of 18), Simplified Read-Only Journal View

### Community 17 - "Fast Onboarding"
Cohesion: 0.67
Nodes (3): 5-Step Onboarding Wizard, Problem: Client Onboarding Takes Hours, Solution: 60-Second Client Onboarding

### Community 18 - "Invite Link Flow"
Cohesion: 1.0
Nodes (2): Client Invite Workflow, Client Invite Link Signup Flow

### Community 19 - "Chart of Accounts"
Cohesion: 1.0
Nodes (2): 24 Indian GAAP Chart of Accounts, Chart of Accounts Section

### Community 20 - "Data Portability"
Cohesion: 1.0
Nodes (2): Problem: Client Data Locked in CA System, Solution: Client-Accessible Portable Data (JSON)

### Community 21 - "Time Tracking Problem"
Cohesion: 1.0
Nodes (2): Problem: No Time Tracking / Billing Justification, Solution: Built-In Time Tracking & Profitability

### Community 22 - "Party Master"
Cohesion: 1.0
Nodes (2): Party Master â€” GSTIN State Auto-Detect, Parties Section

### Community 23 - "Ageing Analysis Section"
Cohesion: 1.0
Nodes (2): Ageing Analysis with Drill-Down & Export, Ageing Analysis Section

### Community 24 - "Module Overview"
Cohesion: 1.0
Nodes (1): Admin Module Overview (18 Modules)

### Community 25 - "Data Architecture"
Cohesion: 1.0
Nodes (1): Data Architecture & Security

### Community 26 - "Market Opportunity"
Cohesion: 1.0
Nodes (1): Market Opportunity â€” $4.2B TAM

### Community 27 - "Business Model"
Cohesion: 1.0
Nodes (1): Business Model â€” Free/Pro/CA Firm Tiers

### Community 28 - "Seed Ask"
Cohesion: 1.0
Nodes (1): Seed Round Ask â€” â‚¹50L

### Community 29 - "Dashboard Section"
Cohesion: 1.0
Nodes (1): Dashboard Section

### Community 30 - "Items Section"
Cohesion: 1.0
Nodes (1): Items & Services Section

### Community 31 - "Setup Section"
Cohesion: 1.0
Nodes (1): Company Setup Section

## Ambiguous Edges - Review These
- `loadAllData` → `Rationale: loadAllData as narrow-waist between persistence and app state`  [AMBIGUOUS]
  graphify-in/kepei-app.js · relation: conceptually_related_to

## Knowledge Gaps
- **55 isolated node(s):** `Admin Module Overview (18 Modules)`, `5-Step Onboarding Wizard`, `Client Invite Workflow`, `Data Architecture & Security`, `Client Invite Link Signup Flow` (+50 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Invite Link Flow`** (2 nodes): `Client Invite Workflow`, `Client Invite Link Signup Flow`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Chart of Accounts`** (2 nodes): `24 Indian GAAP Chart of Accounts`, `Chart of Accounts Section`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Data Portability`** (2 nodes): `Problem: Client Data Locked in CA System`, `Solution: Client-Accessible Portable Data (JSON)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Time Tracking Problem`** (2 nodes): `Problem: No Time Tracking / Billing Justification`, `Solution: Built-In Time Tracking & Profitability`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Party Master`** (2 nodes): `Party Master â€” GSTIN State Auto-Detect`, `Parties Section`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Ageing Analysis Section`** (2 nodes): `Ageing Analysis with Drill-Down & Export`, `Ageing Analysis Section`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Module Overview`** (1 nodes): `Admin Module Overview (18 Modules)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Data Architecture`** (1 nodes): `Data Architecture & Security`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Market Opportunity`** (1 nodes): `Market Opportunity â€” $4.2B TAM`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Business Model`** (1 nodes): `Business Model â€” Free/Pro/CA Firm Tiers`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Seed Ask`** (1 nodes): `Seed Round Ask â€” â‚¹50L`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Dashboard Section`** (1 nodes): `Dashboard Section`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Items Section`** (1 nodes): `Items & Services Section`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Setup Section`** (1 nodes): `Company Setup Section`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `loadAllData` and `Rationale: loadAllData as narrow-waist between persistence and app state`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `toast()` connect `Roles & Invite Flow` to `Data Bootstrap & DB State`, `App Init & Auth`, `Invoice & GST Engine`, `Ageing Analysis & Client Forms`, `OCR Processing`, `Onboarding Wizard`?**
  _High betweenness centrality (0.186) - this node is a cross-community bridge._
- **Why does `loadAllData` connect `Data Bootstrap & DB State` to `Roles & Invite Flow`?**
  _High betweenness centrality (0.160) - this node is a cross-community bridge._
- **Why does `saveModal` connect `Data Bootstrap & DB State` to `Roles & Invite Flow`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._
- **What connects `Admin Module Overview (18 Modules)`, `5-Step Onboarding Wizard`, `Client Invite Workflow` to the rest of the system?**
  _55 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Data Bootstrap & DB State` be split into smaller, more focused modules?**
  _Cohesion score 0.08 - nodes in this community are weakly interconnected._
- **Should `Roles & Invite Flow` be split into smaller, more focused modules?**
  _Cohesion score 0.11 - nodes in this community are weakly interconnected._