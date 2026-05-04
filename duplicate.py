import pandas as pd
data = {
    "name":["Ali","jhon","Ali","sara"],
     "Marks":[80,75,80,90]
}
df = pd.DataFrame(data)
df = df.drop_duplicates()
print(df)