import tabula
import camelot
import json
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.PreCog_DB_a

# File 1c1edeee-a13e-4b2e-90be-eb1dd03c3384.pdf -------------------------

# Get table
path = "./Rec_Task/1c1edeee-a13e-4b2e-90be-eb1dd03c3384.pdf"
dfs = tabula.read_pdf(path, pages='all')

# conversion to required format
dfs_formatted = dfs[0].to_dict()
for i,v in dfs_formatted.items():
    for j,k in v.items():
        j = str(j)
    dfs_formatted[i] = k

# insert into collection
tables_1c1edeee = db["tables_1c1edeee"]
tables_1c1edeee.insert(dfs_formatted)

# -------------------------
