import pandas as pd, csv, sqlite3

dataset_A = pd.read_csv("../dataset_A.csv",index_col=False,names=["id","name","website","phone","email","postal_code","address","country"])
dataset_B = pd.read_csv("../dataset_B.csv",index_col=False,names=["id","name","website","phone","email","postal_code","address","country"])
alldata = []
for index,row in dataset_A.iterrows():
    alldata.append({"source_id" : row.id,"source_name":"dataset_A","name" : row.name,"website" : row.website,"phone" : row.phone,
                    "email" : row.email,"postal_code":row.postal_code,"address":row.address,"country":row.country})
for index,row in dataset_B.iterrows():
    alldata.append({"source_id" : row.id,"source_name":"dataset_B","name" : row.name,"website" : row.website,"phone" : row.phone,
                    "email" : row.email,"postal_code":row.postal_code,"address":row.address,"country":row.country})
pd.DataFrame(alldata).to_sql("companies", sqlite3.connect("../matching_base.sqlite3") ,if_exists="replace")