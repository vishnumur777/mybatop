import pandas as pd
import os

df = pd.read_csv("/opt/mybatop/final.csv")

df.to_xml("data.xml", index=False)

print("XML file saved to: ", os.getcwd())
