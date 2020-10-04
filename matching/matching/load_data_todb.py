import pandas as pd, csv, sqlite3 , time
tic = time.perf_counter() #starting the timer
#connecting to sqlite3 database
sqliteConnection = sqlite3.connect("../matching_base.sqlite3")
cursor = sqliteConnection.cursor()
#removing previous records to avoid repetition
cursor.execute("DELETE FROM companies;")
cursor.execute("DELETE FROM matches;")
sqliteConnection.commit()
cursor.close()
# this file import the csv files 'dataset_A & B' to the database table "companies",
# it also imports the resulting matches from the file "result.csv" to the table "matches"
dataset_A = pd.read_csv("../dataset_A.csv",index_col=False,names=["id","name","website","phone","email","postal_code","address","country"])
dataset_B = pd.read_csv("../dataset_B.csv",index_col=False,names=["id","name","website","phone","email","postal_code","address","country"])
matches_dataset = pd.read_csv("result.csv",index_col=False,names=["dataset_A","dataset_B"])
alldata = [] # this will contain our results
# looping through csv files manually because we need to record the source_name and id of each row before saving
print("parsing csv files... ")
for index,row in dataset_A.iterrows():
    alldata.append({"source_id" : row.id,"source_name":"dataset_A","name" : row.name,"website" : row.website,"phone" : row.phone,
                    "email" : row.email,"postal_code":row.postal_code,"address":row.address,"country":row.country})
for index,row in dataset_B.iterrows():
    alldata.append({"source_id" : row.id,"source_name":"dataset_B","name" : row.name,"website" : row.website,"phone" : row.phone,
                    "email" : row.email,"postal_code":row.postal_code,"address":row.address,"country":row.country})
print("registering to database...")
pd.DataFrame(alldata).to_sql("companies", sqliteConnection,if_exists="replace")
pd.DataFrame(matches_dataset).to_sql("matches",sqliteConnection,if_exists="replace")
toc = time.perf_counter()
print(f"saved data to database in {toc - tic:0.4f} seconds , please check matching_base.sqlite3 tables (companies, matches).")