import pandas as pd
import json
import os

df = pd.read_csv('/opt/mybatop/data/final.csv')

records = df.to_dict(orient='records')
pretty_json = json.dumps(records, indent=4)

with open('data.json', 'w') as f:
    f.write(pretty_json)

print('JSON file saved to: ', os.getcwd())
