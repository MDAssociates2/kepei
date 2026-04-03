"""patch4.py — fix project modalForms, select builder, and saveModal edit support."""
SRC = "C:/Users/Benjamin/kepei/.claude/worktrees/distracted-joliot/index.html"

with open(SRC, "rb") as f:
    data = f.read()

def find_obj_end(data, start):
    """Find end of JS object: skip to first '{', count braces, return pos after closing '}'."""
    i = start
    while i < len(data) and data[i:i+1] != b'{':
        i += 1
    depth = 0
    while i < len(data):
        if data[i:i+1] == b'{':
            depth += 1
        elif data[i:i+1] == b'}':
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return -1

# ── 1. Fix project modalForms ─────────────────────────────────────────────────
proj_start = data.find(b"project:{title:'Create Project'")
print("project entry start:", proj_start)
proj_end = find_obj_end(data, proj_start)
print("project entry end:", proj_end)
OLD_PROJ = data[proj_start:proj_end]
print("OLD len:", len(OLD_PROJ), "preview:", repr(OLD_PROJ[:60]))

NEW_PROJ = (
    b"project:{title:'Create / Edit Project',"
    b"fields:["
    b"{id:'code',label:'Project Code',ph:'PROJ001'},"
    b"{id:'name',label:'Project Name',ph:'Audit FY2025'},"
    b"{id:'client',label:'Client',type:'select',options:[]},"
    b"{id:'engagement_type',label:'Engagement Type',type:'select',options:['Audit','Tax Filing','GST Return','Advisory','Bookkeeping','Other']},"
    b"{id:'billing_method',label:'Billing Method',type:'select',options:['Hourly','Fixed Fee','Non-Billable']},"
    b"{id:'hourly_rate',label:'Hourly Rate',ph:'1500',type:'number'},"
    b"{id:'budget_hours',label:'Budget Hours',ph:'40',type:'number'},"
    b"{id:'due_date',label:'Due Date',type:'date'},"
    b"{id:'status',label:'Status',type:'select',options:['Active','On Hold','Completed','Archived']},"
    b"{id:'assigned_to',label:'Assigned To',ph:'Staff name'}"
    b"],collection:'projects',section:'projects'}"
)

data = data[:proj_start] + NEW_PROJ + data[proj_end:]
print("project modalForms updated, new size:", len(data))

# ── 2. Fix select builder to use DB for client/project fields ─────────────────
OLD_SEL = (
    b"if(f.type==='select'){return`<div class=\"${cls}\"><label>${f.label}</label>"
    b"<select id=\"mf-${f.id}\">${f.options.map(o=>`<option value=\"${typeof o==='string'?o:o}\">"
    b"${typeof o==='string'?o:o}</option>`).join('')}</select></div>`;}"
)
pos = data.find(OLD_SEL)
print("select builder at:", pos)

NEW_SEL = (
    b"if(f.type==='select'){"
    b"var _opts=f.options||[];"
    b"if(f.id==='client'&&type==='project')_opts=(DB.parties||[]).map(function(p){return p.name;});"
    b"if(f.id==='project'&&type==='timeentry')_opts=(DB.projects||[]).filter(function(p){return !p.status||p.status==='Active';}).map(function(p){return p.name;});"
    b"return`<div class=\"${cls}\"><label>${f.label}</label><select id=\"mf-${f.id}\">${_opts.map(function(o){return'<option value=\"'+o+'\">'+o+'</option>';}).join('')}</select></div>`;}"
)

if pos != -1:
    data = data[:pos] + NEW_SEL + data[pos+len(OLD_SEL):]
    print("select builder updated")
else:
    print("WARNING: select builder not found, trying broader search")
    idx = data.find(b"type==='select'")
    print("Found 'type===select' at:", idx)
    print(repr(data[idx:idx+250]))

# ── 3. Fix saveModal: patch all three addRecord calls for edit support ─────────
# 3a. projects-specific
OLD_ADD_PROJ = b"await addRecord('projects', entry);"
NEW_ADD_PROJ = (
    b"if(currentEditId){await updateRecord('projects',currentEditId,entry);"
    b"currentEditId=null;}else{await addRecord('projects',entry);}"
)
if OLD_ADD_PROJ in data:
    data = data.replace(OLD_ADD_PROJ, NEW_ADD_PROJ, 1)
    print("saveModal projects edit support added")
else:
    print("WARNING: projects addRecord pattern not found")

# 3b. time_entries-specific
OLD_ADD_TE = b"await addRecord('time_entries', entry);"
NEW_ADD_TE = (
    b"if(currentEditId){await updateRecord('time_entries',currentEditId,entry);"
    b"currentEditId=null;}else{await addRecord('time_entries',entry);}"
)
if OLD_ADD_TE in data:
    data = data.replace(OLD_ADD_TE, NEW_ADD_TE, 1)
    print("saveModal time_entries edit support added")
else:
    print("WARNING: time_entries addRecord pattern not found")

# 3c. generic cfg.collection
OLD_ADD_CFG = b"await addRecord(cfg.collection, entry);"
NEW_ADD_CFG = (
    b"if(currentEditId){await updateRecord(cfg.collection,currentEditId,entry);"
    b"currentEditId=null;}else{await addRecord(cfg.collection,entry);}"
)
if OLD_ADD_CFG in data:
    data = data.replace(OLD_ADD_CFG, NEW_ADD_CFG, 1)
    print("saveModal generic edit support added")
else:
    print("WARNING: generic addRecord pattern not found")

with open(SRC, "wb") as f:
    f.write(data)
print(f"Done. File: {len(data)} bytes")
