# Kepei Knowledge Graph — Index

> **217 nodes · 346 edges · 28 communities** · deep-mode extraction

## Architectural seams (documented)

- **`loadAllData`** — sole READ-hydration path on startup. See function JSDoc.
- **`saveModal`** — modal write dispatcher. See function JSDoc. Known issue: invoice branch writes 3 collections without `db.batch()`.

Both docstrings are extracted into this graph as `sole_writer_of` / `writes_to` / `implements` / `technical_debt_of` edges. The tension between them (loadAllData claims sole ownership; saveModal also writes via addRecord) is captured as a `conflicts_with` edge — this is intentional, it marks an architectural nuance worth knowing.

---

## Communities

### Auth & Roles (48 nodes · cohesion 0.06)
- Graphify In Js
- Acceptocrresult
- Checkinviteparam
- Closeocrmodal
- Dologin
- _...and 43 more_

### Data Bootstrap & DB State (31 nodes · cohesion 0.07)
- Db Coa
- Db Fixed Assets
- Db Gst Ledger
- Db Inventory
- Db Invites
- _...and 26 more_

### Auth & Roles (25 nodes · cohesion 0.11)
- Addrecord
- Applyrole
- Closemodal
- Completesignup
- Copyinvitelink
- _...and 20 more_

### OCR Processing (18 nodes · cohesion 0.16)
- Closeclientform
- Displayocrresult
- Drillpartyageing
- Esc
- Extractocrfields
- _...and 13 more_

### Section Loaders (15 nodes · cohesion 0.16)
- Formatcurrency
- Getclientprojects
- Initapp
- Loaddashboard
- Loadtimereports
- _...and 10 more_

### Modal Dispatcher & Writes (14 nodes · cohesion 0.14)
- Deep Dive Fixed Assets Tds
- Deep Dive Gst Engine
- Deep Dive Invoice Three Records
- Deep Dive Stock Register
- Problems Solution One Invoice Three
- _...and 9 more_

### Modal Dispatcher & Writes (13 nodes · cohesion 0.21)
- Addinvoiceline
- Applyocrtoclientform
- Getgstregime
- Getinvoicetypeoptions
- Getlineitemheaders
- _...and 8 more_

### Section Loaders (11 nodes · cohesion 0.18)
- Deep Dive Dashboard Zero Load
- Features Competitive Matrix
- Features Firestore Scalability
- Features India First Gst
- Features Zero Infrastructure
- _...and 6 more_

### Section Loaders (6 nodes · cohesion 0.47)
- Calcageingdata
- Exportageingdata
- Loadageinganalysis
- Renderageingsummary
- Renderageingtable
- _...and 1 more_

### Product Documentation (5 nodes · cohesion 0.40)
- Deep Dive User Management Multitenant
- Pitch Deck Ca Distribution
- Problems Multi Client Nightmare
- Problems Solution Multitenant
- Sections Users

### Product Documentation (4 nodes · cohesion 0.50)
- Deep Dive Projects Time
- Sections Projects
- Sections Timeentries
- Sections Timereports

### Cluster 11 (3 nodes · cohesion 0.67)
- Ca Admin Guide Admin Vs Client Roles
- Client Orientation Client Modules
- Client Orientation Simplified Journal

### Product Positioning (3 nodes · cohesion 0.67)
- Ca Admin Guide Onboarding Wizard
- Problems Client Onboarding Hours
- Problems Solution 60S Onboarding

### Auth & Roles (2 nodes · cohesion 1.00)
- Ca Admin Guide Client Invite Workflow
- Client Orientation Invite Link

### Ageing Analysis (2 nodes · cohesion 1.00)
- Deep Dive Ageing Analysis
- Sections Ageing

### Product Positioning (2 nodes · cohesion 1.00)
- Problems Data Locked Ca
- Problems Solution Portable Data

### Product Positioning (2 nodes · cohesion 1.00)
- Problems No Time Tracking
- Problems Solution Builtin Time

### Product Documentation (2 nodes · cohesion 1.00)
- Deep Dive Party Master
- Sections Parties

### Product Documentation (2 nodes · cohesion 1.00)
- Deep Dive Coa 24 Accounts
- Sections Coa

### Cluster 19 (1 nodes · cohesion 1.00)
- Ca Admin Guide Module Overview

### Cluster 20 (1 nodes · cohesion 1.00)
- Ca Admin Guide Data Architecture

### Product Positioning (1 nodes · cohesion 1.00)
- Pitch Deck Market Opportunity

### Product Positioning (1 nodes · cohesion 1.00)
- Pitch Deck Business Model

### Product Positioning (1 nodes · cohesion 1.00)
- Pitch Deck Seed Ask

### Cluster 24 (1 nodes · cohesion 1.00)
- Sections Dashboard

### Cluster 25 (1 nodes · cohesion 1.00)
- Sections Items

### Cluster 26 (1 nodes · cohesion 1.00)
- Sections Setup

### Cluster 27 (1 nodes · cohesion 1.00)
- Savealldata

---

## God Nodes

- **Toast**
- **Savemodal**
- **Loadalldata**
- **Openmodal**
- **Isadmin**
- **Fmt**
- **Savemodal**
- **Esc**
- **Updatebadges**
- **Renderreport**

---

## Surprising Connections

- {'source': 'saveModal', 'target': 'toast()', 'source_files': ['graphify-in/kepei-app.js', 'graphify-in\\kepei-app.js'], 'confidence': 'EXTRACTED', 'relation': 'calls', 'why': 'connects across different repos/directories; bridges separate communities'}
- {'source': '5-Step Onboarding Wizard', 'target': 'Solution: 60-Second Client Onboarding', 'source_files': ['graphify-in/Kepei-CA-Admin-Guide.md', 'graphify-in/Kepei-Problems-Solutions.md'], 'confidence': 'INFERRED', 'relation': 'semantically_similar_to', 'why': 'inferred connection - not explicitly stated in source; semantically similar concepts with no structural link'}
- {'source': 'Solution: One Invoice = Three Auto-Records', 'target': 'One Invoice = Three Auto-Created Records', 'source_files': ['graphify-in/Kepei-Problems-Solutions.md', 'graphify-in/Kepei-Deep-Dive.md'], 'confidence': 'INFERRED', 'relation': 'semantically_similar_to', 'why': 'inferred connection - not explicitly stated in source; semantically similar concepts with no structural link'}
- {'source': 'Solution: Multi-Tenant Architecture', 'target': 'Multi-Tenant User Management Architecture', 'source_files': ['graphify-in/Kepei-Problems-Solutions.md', 'graphify-in/Kepei-Deep-Dive.md'], 'confidence': 'INFERRED', 'relation': 'semantically_similar_to', 'why': 'inferred connection - not explicitly stated in source; semantically similar concepts with no structural link'}
- {'source': 'Dashboard Zero-Load Architecture', 'target': 'Zero Infrastructure â€” Single HTML File', 'source_files': ['graphify-in/Kepei-Deep-Dive.md', 'graphify-in/Kepei-Features.md'], 'confidence': 'INFERRED', 'relation': 'semantically_similar_to', 'why': 'inferred connection - not explicitly stated in source; semantically similar concepts with no structural link'}

---

## Suggested Questions

- {'type': 'bridge_node', 'question': 'Why does `saveModal` connect `Data Bootstrap & DB State` to `Auth & Roles`?', 'why': 'High betweenness centrality (0.175) - this node is a cross-community bridge.'}
- {'type': 'bridge_node', 'question': 'Why does `toast()` connect `Auth & Roles` to `Auth & Roles`, `Data Bootstrap & DB State`, `OCR Processing`, `Section Loaders`, `Modal Dispatcher & Writes`, `Section Loaders`?', 'why': 'High betweenness centrality (0.168) - this node is a cross-community bridge.'}
- {'type': 'verify_inferred', 'question': 'Are the 4 inferred relationships involving `saveModal` (e.g. with `DB.invoices` and `DB.inventory`) actually correct?', 'why': '`saveModal` has 4 INFERRED edges - model-reasoned connections that need verification.'}
- {'type': 'isolated_nodes', 'question': 'What connects `Admin Module Overview (18 Modules)`, `5-Step Onboarding Wizard`, `Client Invite Workflow` to the rest of the system?', 'why': '66 weakly-connected nodes found - possible documentation gaps or missing edges.'}
- {'type': 'low_cohesion', 'question': 'Should `Auth & Roles` be split into smaller, more focused modules?', 'why': 'Cohesion score 0.06 - nodes in this community are weakly interconnected.'}
- {'type': 'low_cohesion', 'question': 'Should `Data Bootstrap & DB State` be split into smaller, more focused modules?', 'why': 'Cohesion score 0.07 - nodes in this community are weakly interconnected.'}

---

## Quick Links

- [GRAPH_REPORT.md](../GRAPH_REPORT.md) — full audit report
- [graph.html](../graph.html) — interactive visualization
