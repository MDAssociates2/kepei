---
type: community
cohesion: 0.16
members: 21
---

# Invoice & GST Engine

**Cohesion:** 0.16 - loosely connected
**Members:** 21 nodes

## Members
- [[addInvoiceLine()]] - code - graphify-in\kepei-app.js
- [[closeModal()]] - code - graphify-in\kepei-app.js
- [[createUserAccount()]] - code - graphify-in\kepei-app.js
- [[determineInvoiceTypes()]] - code - graphify-in\kepei-app.js
- [[getBuyerGSTProfile()]] - code - graphify-in\kepei-app.js
- [[getGSTRegime()]] - code - graphify-in\kepei-app.js
- [[getInvoiceTypeOptions()]] - code - graphify-in\kepei-app.js
- [[getLineItemHeaders()]] - code - graphify-in\kepei-app.js
- [[getNextInvoiceNumber()]] - code - graphify-in\kepei-app.js
- [[getNextProjectNumber()]] - code - graphify-in\kepei-app.js
- [[getRegimeBanner()]] - code - graphify-in\kepei-app.js
- [[getSellerGSTProfile()]] - code - graphify-in\kepei-app.js
- [[getStateFromGSTIN()]] - code - graphify-in\kepei-app.js
- [[isInterState()]] - code - graphify-in\kepei-app.js
- [[openModal()]] - code - graphify-in\kepei-app.js
- [[recalculateInvoice()]] - code - graphify-in\kepei-app.js
- [[refreshInvoiceTypeOnPartyChange()]] - code - graphify-in\kepei-app.js
- [[removeInvoiceLine()]] - code - graphify-in\kepei-app.js
- [[renderInvoiceGuidance()]] - code - graphify-in\kepei-app.js
- [[saveModal()]] - code - graphify-in\kepei-app.js
- [[updatePartyDetails()]] - code - graphify-in\kepei-app.js

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Invoice_&_GST_Engine
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_App Init & Auth]]
- 6 edges to [[_COMMUNITY_Roles & Invite Flow]]
- 3 edges to [[_COMMUNITY_Ageing Analysis & Client Forms]]
- 1 edge to [[_COMMUNITY_Navigation & OCR Modal]]

## Top bridge nodes
- [[saveModal()]] - degree 12, connects to 4 communities
- [[openModal()]] - degree 13, connects to 3 communities
- [[refreshInvoiceTypeOnPartyChange()]] - degree 9, connects to 2 communities
- [[determineInvoiceTypes()]] - degree 8, connects to 1 community
- [[getBuyerGSTProfile()]] - degree 6, connects to 1 community