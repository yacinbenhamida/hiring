import pandas as pd
import numpy as np
dataset_A = pd.read_csv("../dataset_A.csv", names=["id","name","website","code","phone","zip","address","country"])
dataset_B = pd.read_csv("../dataset_B.csv", names=["id","name","website","code","phone","zip","address","country"])
#id | name | site  web | unkown | num tel | addr | zip | country 



matches = dataset_A.merge(dataset_B)
print(matches.head(5))

matches.to_csv('result.csv')

