import tabula
import camelot
import json
import pymongo
import math

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
        dfs_formatted[i] = k

# insert into collection
tables_1c1edeee = db["tables_1c1edeee"]
tables_1c1edeee.insert(dfs_formatted)

# -------------------------

# File 1c1edeee-a13e-4b2e-90be-eb1dd03c3384.pdf -------------------------

# Get table
path = "./Rec_Task/a6b29367-f3b7-4fb1-a2d0-077477eac1d9.pdf"
dfs = tabula.read_pdf(path, pages='all')

# conversion to required format
dfs_formatted = dfs[0].to_dict()

for i,v in dfs_formatted.items():
    temp = []
    for j,k in v.items():
        if isinstance(k, str):
            temp.append(k)

    dfs_formatted[i] = "\n".join(temp)

# insert into collection
tables_a6b29367 = db["tables_a6b29367"]
tables_a6b29367.insert(dfs_formatted)

# -------------------------
