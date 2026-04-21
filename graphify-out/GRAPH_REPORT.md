# Graph Report - .  (2026-04-21)

## Corpus Check
- Corpus is ~20,787 words - fits in a single context window. You may not need a graph.

## Summary
- 217 nodes · 346 edges · 28 communities detected
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 16 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Auth & Roles|Auth & Roles]]
- [[_COMMUNITY_Data Bootstrap & DB State|Data Bootstrap & DB State]]
- [[_COMMUNITY_Auth & Roles|Auth & Roles]]
- [[_COMMUNITY_OCR Processing|OCR Processing]]
- [[_COMMUNITY_Section Loaders|Section Loaders]]
- [[_COMMUNITY_Modal Dispatcher & Writes|Modal Dispatcher & Writes]]
- [[_COMMUNITY_Modal Dispatcher & Writes|Modal Dispatcher & Writes]]
- [[_COMMUNITY_Section Loaders|Section Loaders]]
- [[_COMMUNITY_Section Loaders|Section Loaders]]
- [[_COMMUNITY_Product Documentation|Product Documentation]]
- [[_COMMUNITY_Product Documentation|Product Documentation]]
- [[_COMMUNITY_Cluster 11|Cluster 11]]
- [[_COMMUNITY_Product Positioning|Product Positioning]]
- [[_COMMUNITY_Auth & Roles|Auth & Roles]]
- [[_COMMUNITY_Ageing Analysis|Ageing Analysis]]
- [[_COMMUNITY_Product Positioning|Product Positioning]]
- [[_COMMUNITY_Product Positioning|Product Positioning]]
- [[_COMMUNITY_Product Documentation|Product Documentation]]
- [[_COMMUNITY_Product Documentation|Product Documentation]]
- [[_COMMUNITY_Cluster 19|Cluster 19]]
- [[_COMMUNITY_Cluster 20|Cluster 20]]
- [[_COMMUNITY_Product Positioning|Product Positioning]]
- [[_COMMUNITY_Product Positioning|Product Positioning]]
- [[_COMMUNITY_Product Positioning|Product Positioning]]
- [[_COMMUNITY_Cluster 24|Cluster 24]]
- [[_COMMUNITY_Cluster 25|Cluster 25]]
- [[_COMMUNITY_Cluster 26|Cluster 26]]
- [[_COMMUNITY_Cluster 27|Cluster 27]]

## God Nodes (most connected - your core abstractions)
1. `toast()` - 18 edges
2. `saveModal` - 17 edges
3. `loadAllData` - 16 edges
4. `openModal()` - 12 edges
5. `isAdmin()` - 11 edges
6. `fmt()` - 11 edges
7. `saveModal()` - 9 edges
8. `esc()` - 8 edges
9. `updateBadges()` - 8 edges
10. `renderReport()` - 8 edges

## Surprising Connections (you probably didn't know these)
- `saveModal` --calls--> `toast()`  [EXTRACTED]
  graphify-in/kepei-app.js → graphify-in\kepei-app.js
- `5-Step Onboarding Wizard` --semantically_similar_to--> `Solution: 60-Second Client Onboarding`  [INFERRED] [semantically similar]
  graphify-in/Kepei-CA-Admin-Guide.md → graphify-in/Kepei-Problems-Solutions.md
- `Solution: One Invoice = Three Auto-Records` --semantically_similar_to--> `One Invoice = Three Auto-Created Records`  [INFERRED] [semantically similar]
  graphify-in/Kepei-Problems-Solutions.md → graphify-in/Kepei-Deep-Dive.md
- `Solution: Multi-Tenant Architecture` --semantically_similar_to--> `Multi-Tenant User Management Architecture`  [INFERRED] [semantically similar]
  graphify-in/Kepei-Problems-Solutions.md → graphify-in/Kepei-Deep-Dive.md
- `Dashboard Zero-Load Architecture` --semantically_similar_to--> `Zero Infrastructure â€” Single HTML File`  [INFERRED] [semantically similar]
  graphify-in/Kepei-Deep-Dive.md → graphify-in/Kepei-Features.md

## Hyperedges (group relationships)
- **30 Problem-Solution Pairs (Core Product Rationale)** — problems_triple_data_entry, problems_solution_one_invoice_three, problems_gst_manual_error_prone, problems_solution_gst_engine, problems_multi_client_nightmare, problems_solution_multitenant [EXTRACTED 1.00]
- **Invoice â†’ Journal + GST Ledger + Stock Entry Auto-Creation** — kepei_app_saveModal, kepei_app_addRecord, kepei_app_DB_invoices, kepei_app_DB_inventory, kepei_app_DB_gst_ledger [EXTRACTED 0.90]

## Communities

### Community 0 - "Auth & Roles"
Cohesion: 0.06
Nodes (29): acceptOCRResult(), closeOCRModal(), filterGST(), generateInvoiceHTML(), genRecs(), initWizard(), loadBulkEntry(), loadGSTLedger() (+21 more)

### Community 1 - "Data Bootstrap & DB State"
Cohesion: 0.07
Nodes (31): DB.coa, DB.fixed_assets, DB.gst_ledger, DB.inventory, DB.invites, DB.invoices, DB.items, DB.parties (+23 more)

### Community 2 - "Auth & Roles"
Cohesion: 0.11
Nodes (25): addRecord(), applyRole(), closeModal(), completeSignup(), copyInviteLink(), copyToClipboard(), createUserAccount(), deleteEntry() (+17 more)

### Community 3 - "OCR Processing"
Cohesion: 0.16
Nodes (18): closeClientForm(), displayOCRResult(), drillPartyAgeing(), esc(), extractOCRFields(), fmt(), handleOCRDrop(), handleOCRFile() (+10 more)

### Community 4 - "Section Loaders"
Cohesion: 0.16
Nodes (15): formatCurrency(), getClientProjects(), initApp(), loadDashboard(), loadTimeReports(), renderClientBilling(), renderDetailedLog(), renderProfitability() (+7 more)

### Community 5 - "Modal Dispatcher & Writes"
Cohesion: 0.14
Nodes (14): Fixed Assets & TDS Module, GST Engine: CGST/SGST/IGST Auto-Split, One Invoice = Three Auto-Created Records, Stock Register â€” Invoice-Driven Automation, Solution: One Invoice = Three Auto-Records, Problem: Triple Data Entry (Invoice+GST+Stock), Fixed Assets Section, GST Ledger Section (+6 more)

### Community 6 - "Modal Dispatcher & Writes"
Cohesion: 0.21
Nodes (13): addInvoiceLine(), applyOCRToClientForm(), getGSTRegime(), getInvoiceTypeOptions(), getLineItemHeaders(), getNextInvoiceNumber(), getRegimeBanner(), openClientForm() (+5 more)

### Community 7 - "Section Loaders"
Cohesion: 0.18
Nodes (11): Dashboard Zero-Load Architecture, Feature Matrix vs Tally/Zoho/Vyapar, Firestore Subcollection Scalability, India-First GST Engine (Core Architecture), Zero Infrastructure â€” Single HTML File, Problem: 63M MSMEs Lack GST-Ready Software, Scale Roadmap (v3 â†’ API â†’ PWA â†’ White-label), Problem: Client Has No Book Visibility (+3 more)

### Community 8 - "Section Loaders"
Cohesion: 0.47
Nodes (6): calcAgeingData(), exportAgeingData(), loadAgeingAnalysis(), renderAgeingSummary(), renderAgeingTable(), switchAgeingTab()

### Community 9 - "Product Documentation"
Cohesion: 0.4
Nodes (5): Multi-Tenant User Management Architecture, CA Firm as Distribution Channel, Problem: Managing Multiple Clients is Difficult, Solution: Multi-Tenant Architecture, User Management Section

### Community 10 - "Product Documentation"
Cohesion: 0.5
Nodes (4): Projects & Time Tracking (3 Entry Modes), Projects Section, Time Entries Section, Time Reports Section

### Community 11 - "Cluster 11"
Cohesion: 0.67
Nodes (3): Admin vs Client Role Separation, Client-Visible Modules (8 of 18), Simplified Read-Only Journal View

### Community 12 - "Product Positioning"
Cohesion: 0.67
Nodes (3): 5-Step Onboarding Wizard, Problem: Client Onboarding Takes Hours, Solution: 60-Second Client Onboarding

### Community 13 - "Auth & Roles"
Cohesion: 1.0
Nodes (2): Client Invite Workflow, Client Invite Link Signup Flow

### Community 14 - "Ageing Analysis"
Cohesion: 1.0
Nodes (2): Ageing Analysis with Drill-Down & Export, Ageing Analysis Section

### Community 15 - "Product Positioning"
Cohesion: 1.0
Nodes (2): Problem: Client Data Locked in CA System, Solution: Client-Accessible Portable Data (JSON)

### Community 16 - "Product Positioning"
Cohesion: 1.0
Nodes (2): Problem: No Time Tracking / Billing Justification, Solution: Built-In Time Tracking & Profitability

### Community 17 - "Product Documentation"
Cohesion: 1.0
Nodes (2): Party Master â€” GSTIN State Auto-Detect, Parties Section

### Community 18 - "Product Documentation"
Cohesion: 1.0
Nodes (2): 24 Indian GAAP Chart of Accounts, Chart of Accounts Section

### Community 19 - "Cluster 19"
Cohesion: 1.0
Nodes (1): Admin Module Overview (18 Modules)

### Community 20 - "Cluster 20"
Cohesion: 1.0
Nodes (1): Data Architecture & Security

### Community 21 - "Product Positioning"
Cohesion: 1.0
Nodes (1): Market Opportunity â€” $4.2B TAM

### Community 22 - "Product Positioning"
Cohesion: 1.0
Nodes (1): Business Model â€” Free/Pro/CA Firm Tiers

### Community 23 - "Product Positioning"
Cohesion: 1.0
Nodes (1): Seed Round Ask â€” â‚¹50L

### Community 24 - "Cluster 24"
Cohesion: 1.0
Nodes (1): Dashboard Section

### Community 25 - "Cluster 25"
Cohesion: 1.0
Nodes (1): Items & Services Section

### Community 26 - "Cluster 26"
Cohesion: 1.0
Nodes (1): Company Setup Section

### Community 27 - "Cluster 27"
Cohesion: 1.0
Nodes (1): saveAllData

## Knowledge Gaps
- **66 isolated node(s):** `Admin Module Overview (18 Modules)`, `5-Step Onboarding Wizard`, `Client Invite Workflow`, `Data Architecture & Security`, `Client Invite Link Signup Flow` (+61 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Auth & Roles`** (2 nodes): `Client Invite Workflow`, `Client Invite Link Signup Flow`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Ageing Analysis`** (2 nodes): `Ageing Analysis with Drill-Down & Export`, `Ageing Analysis Section`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Product Positioning`** (2 nodes): `Problem: Client Data Locked in CA System`, `Solution: Client-Accessible Portable Data (JSON)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Product Positioning`** (2 nodes): `Problem: No Time Tracking / Billing Justification`, `Solution: Built-In Time Tracking & Profitability`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Product Documentation`** (2 nodes): `Party Master â€” GSTIN State Auto-Detect`, `Parties Section`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Product Documentation`** (2 nodes): `24 Indian GAAP Chart of Accounts`, `Chart of Accounts Section`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Cluster 19`** (1 nodes): `Admin Module Overview (18 Modules)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Cluster 20`** (1 nodes): `Data Architecture & Security`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Product Positioning`** (1 nodes): `Market Opportunity â€” $4.2B TAM`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Product Positioning`** (1 nodes): `Business Model â€” Free/Pro/CA Firm Tiers`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Product Positioning`** (1 nodes): `Seed Round Ask â€” â‚¹50L`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Cluster 24`** (1 nodes): `Dashboard Section`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Cluster 25`** (1 nodes): `Items & Services Section`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Cluster 26`** (1 nodes): `Company Setup Section`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Cluster 27`** (1 nodes): `saveAllData`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `saveModal` connect `Data Bootstrap & DB State` to `Auth & Roles`?**
  _High betweenness centrality (0.175) - this node is a cross-community bridge._
- **Why does `toast()` connect `Auth & Roles` to `Auth & Roles`, `Data Bootstrap & DB State`, `OCR Processing`, `Section Loaders`, `Modal Dispatcher & Writes`, `Section Loaders`?**
  _High betweenness centrality (0.168) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `saveModal` (e.g. with `DB.invoices` and `DB.inventory`) actually correct?**
  _`saveModal` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Admin Module Overview (18 Modules)`, `5-Step Onboarding Wizard`, `Client Invite Workflow` to the rest of the system?**
  _66 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Auth & Roles` be split into smaller, more focused modules?**
  _Cohesion score 0.06 - nodes in this community are weakly interconnected._
- **Should `Data Bootstrap & DB State` be split into smaller, more focused modules?**
  _Cohesion score 0.07 - nodes in this community are weakly interconnected._
- **Should `Auth & Roles` be split into smaller, more focused modules?**
  _Cohesion score 0.11 - nodes in this community are weakly interconnected._