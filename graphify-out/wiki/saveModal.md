---
source_file: "graphify-in/kepei-app.js"
type: "code"
community: "Data Bootstrap & DB State"
location: "L1329"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Data_Bootstrap_&_DB_State
---

# saveModal

## Connections
- [[DB.gst_ledger]] - `writes_to` [INFERRED]
- [[DB.inventory]] - `writes_to` [INFERRED]
- [[DB.invoices]] - `writes_to` [INFERRED]
- [[Non-atomic invoice write (missing db.batch)]] - `technical_debt_of` [EXTRACTED]
- [[__user__ modal]] - `implements` [EXTRACTED]
- [[addRecord]] - `calls` [EXTRACTED]
- [[closeModal]] - `calls` [EXTRACTED]
- [[createUserAccount]] - `calls` [EXTRACTED]
- [[gstentry modal]] - `implements` [EXTRACTED]
- [[invoice modal (3-record atomic)]] - `implements` [EXTRACTED]
- [[loadAllData]] - `conflicts_with` [INFERRED]
- [[modalForms config]] - `references` [EXTRACTED]
- [[project modal]] - `implements` [EXTRACTED]
- [[stockentry modal]] - `implements` [EXTRACTED]
- [[timeentry modal]] - `implements` [EXTRACTED]
- [[toast()]] - `calls` [EXTRACTED]
- [[updateRecord]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Data_Bootstrap_&_DB_State