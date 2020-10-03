import pandas as pd , math,numpy as np, csv

dataset_A = pd.read_csv("../dataset_A.csv",index_col=False,names=["id","name","website","phone","code","zip","address","country"])
dataset_A.website=dataset_A.website.astype(str).apply(lambda f: f.lower())
dataset_A.name=dataset_A.name.apply(lambda f: f.lower()).astype(str)
dataset_B = pd.read_csv("../dataset_B.csv",index_col=False,names=["id","name","website","phone","code","zip","address","country"])
dataset_B.website=dataset_B.website.astype(str).apply(lambda f: f.lower())
dataset_B.name=dataset_B.name.astype(str).apply(lambda f: f.lower())
for index,row in dataset_A.iterrows():
    if((row['name']!="nan" and row['name']!="") or (row['website']!="nan" and row['website']!=""))  :
        matches = dataset_B.loc[ (row["name"] == dataset_B["name"])
                                & (row["website"] == dataset_B["website"] )
                                ]
        if matches.size > 0:
            with open('result.csv','a',newline='') as csvfile:
                fieldnames = ['source_A','source_B']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for ind,join in matches.iterrows():
                    writer.writerow({"source_A":row["id"] , "source_B" : join["id"]})
                    



