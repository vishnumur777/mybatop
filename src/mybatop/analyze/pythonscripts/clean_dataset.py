import pandas as pd
import os


df1 = pd.read_csv("data.csv")

mask = df1["SERIAL_NUMBER"].isnull()

cols = df1.columns.tolist()

curr_idx = cols.index("CURRENT_NOW")

col1 = df1.columns[:curr_idx]
col2 = df1.columns[curr_idx:]

df1.SERIAL_NUMBER = df1.SERIAL_NUMBER.astype(str)

df1.loc[mask, col2] = df1.loc[mask, col2].shift(axis=1)

df1.loc[mask, "CURRENT_NOW"] = df1.loc[mask, "CURRENT_NOW"].fillna(0)

# Save the modified dataframe (optional)
df1.to_csv("final_fixed.csv", index=False)

os.system("rm -rf data.csv")

os.system("mv final_fixed.csv data.csv")
