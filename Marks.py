import pandas as pd
df=pd.read_excel("day14.xlsx")
df["mark"]=df["mark"]+10
print(df)
df.to_excel("day14_updated.xlsx", index=False)
print("DataFrame loaded successfully.")