import pandas as pd
import numpy as np
dataset_A = pd.read_csv("../dataset_A.csv", names=["id","name","website","code","phone","zip","address","country"])
dataset_B = pd.read_csv("../dataset_B.csv", names=["id","name","website","code","phone","zip","address","country"])
#id | name | site  web | unkown | num tel | addr | zip | country 


keys = ["id","name","website","phone","address","zip","country"]
columns = [col for col in dataset_A.columns if col not in keys]

selected_columns = keys.copy()
selected_columns.extend(columns)

dsA = dataset_A[selected_columns].set_index(keys)
dsB = dataset_B[selected_columns].set_index(keys)

dataset_A.update(dataset_B)
mask = np.equal(dsA[columns].values, dsA.values).all(axis=1)

matches = dataset_A[mask]
print(matches.head(5))
matchesD = matches.drop_duplicates(subset=['name','website',"phone",'zip','address'],keep='first')
print('duplicate rows')
print(matchesD)
matchesD.to_csv('result.csv')

