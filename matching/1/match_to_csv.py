import pandas as pd , math,numpy as np, csv, sqlite3 , time
tic = time.perf_counter() #starting the timer

#loading datasets from csv files
dataset_A = pd.read_csv("../dataset_A.csv",index_col=False,names=["id","name","website","phone","code","postal_code","address","country"])
dataset_B = pd.read_csv("../dataset_B.csv",index_col=False,names=["id","name","website","phone","code","postal_code","address","country"])

#converting website & name columns to str and making sure they are in lowercase
dataset_A.website=dataset_A.website.astype(str).apply(lambda f: f.lower())
dataset_A.name=dataset_A.name.apply(lambda f: f.lower()).astype(str)
dataset_B.website=dataset_B.website.astype(str).apply(lambda f: f.lower())
dataset_B.name=dataset_B.name.astype(str).apply(lambda f: f.lower())

#looping through the first dataset_A
for index,row in dataset_A.iterrows():
    #testing if the current row from dataset_A appears in dataset_B
    if((row['name']!="nan" and row['name']!="") or (row['website']!="nan" and row['website']!=""))  :
        matches = dataset_B.loc[ (row["name"] == dataset_B["name"])
                                & (row["website"] == dataset_B["website"] )
                                ]
        if matches.size > 0:
            #writing the result to a csv file
            with open('result.csv','a',newline='') as csvfile:
                fieldnames = ['source_A','source_B']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for ind,join in matches.iterrows():
                    print(row["name"]+" matches with "+join["name"])
                    writer.writerow({"source_A":row["id"] , "source_B" : join["id"]})                   
toc = time.perf_counter()
print(f"computed matches in {toc - tic:0.4f} seconds")

