import csv
import pandas as pd
data = {"Name": ["tuvshin", "tur", "Lkhadorj", "Tsendsuren", "Tuvshintur"], 
        "Age": [23, 21, 25, 23, 22]}
data = pd.DataFrame(data)
data.to_csv("age_data.csv", index=False)
print(data.head())