import pandas as pd
import json
import argparse

def capacity():

    df = pd.read_csv("data.csv")

    df["DATETIME"] = df["DATE"]+" "+df["TIME"]

    df["DATETIME"] = pd.to_datetime(df["DATETIME"],format="%m/%d/%y %H:%M:%S")

    df1 = df[["DATETIME","CHARGE_FULL", "CHARGE_FULL_DESIGN"]].copy()

    prev_charge_full = df1["CHARGE_FULL"].iloc[0].copy()

    grp = 1

    for i in range(len(df1)):
        if df1["CHARGE_FULL"].iloc[i] == prev_charge_full:
            df1.loc[i,"GROUP"] = grp
        else:
            prev_charge_full = df1["CHARGE_FULL"].iloc[i]
            grp += 1
    
    df1_gr = pd.DataFrame()

    df1_gr["START_DATE"] = df1.groupby("GROUP").agg({"DATETIME":"first"})

    df1_gr["END_DATE"] = df1.groupby("GROUP").agg({"DATETIME":"last"})

    df1_gr["CHARGE_FULL(mAh)"] = df1.groupby("GROUP").agg({"CHARGE_FULL":"first"})

    df1_gr["CHARGE_FULL_DESIGN(mAh)"] = df1.groupby("GROUP").agg({"CHARGE_FULL_DESIGN":"first"})

    df1_gr["CHARGE_FULL(mAh)"] = (df1_gr["CHARGE_FULL(mAh)"] / 1000).astype(int).astype(str)
    
    df1_gr["CHARGE_FULL_DESIGN(mAh)"] = (df1_gr["CHARGE_FULL_DESIGN(mAh)"] / 1000).astype(int).astype(str)

    df1_gr.reset_index(drop=True, inplace=True)

    usage_df = df[["DATETIME", "STATE", "STATUS"]].copy()

    usage_df["GROUP"] = df1["GROUP"].copy()

    usage_df.to_csv("batusageact.csv", index=False)

    return df1_gr

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--html", action="store_true")

    parser.add_argument("--csv", action="store_true")

    parser.add_argument("--xml", action="store_true")

    parser.add_argument("--json", action="store_true")

    args = parser.parse_args()

    caphistory = capacity()

    caphistory["START_DATE"] = pd.to_datetime(caphistory["START_DATE"])

    caphistory["END_DATE"] = pd.to_datetime(caphistory["END_DATE"])

    if args.html:

        caphistory.to_html("d.html",index=False)

    elif args.csv:

        caphistory.to_csv("index.csv",index=False)

    elif args.xml:

        caphistory.columns = ["START_DATE","END_DATE","CHARGE_FULL","CHARGE_FULL_DESIGN"]

        caphistory.to_xml("index.xml",index=False)

    elif args.json:

        records = caphistory.to_dict(orient='records')
        pretty_json = json.dumps(records, indent=4)

        with open('index.json', 'w') as f:
            f.write(pretty_json)
