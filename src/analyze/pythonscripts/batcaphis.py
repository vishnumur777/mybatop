import pandas as pd
import json
import argparse

def capacity():

    date_format = '%m/%d/%y'

    caphis = pd.read_csv("data.csv",parse_dates=["DATE"],index_col="DATE",date_format=date_format)

    caphistory = pd.DataFrame()

    caphis.dropna(subset=["SERIAL_NUMBER"],inplace=True)

    caphis.head(5)

    caphis =  caphis[["CHARGE_FULL","CHARGE_FULL_DESIGN"]]

    caphis["CHARGE_FULL"] = (caphis["CHARGE_FULL"]/1000).astype(int)

    caphis["CHARGE_FULL_DESIGN"] = (caphis["CHARGE_FULL_DESIGN"]/1000).astype(int)

    curr_date=pd.to_datetime(caphis.index[-1])

    week_d=curr_date+pd.DateOffset(weeks=1)

    st_l = []
    en_l = []
    ch_l = []

    while True:
        st_l.append(curr_date)

        en_l.append(week_d)

        ch_l.append(caphis.loc[(caphis.index>=curr_date)&(caphis.index<=week_d)]["CHARGE_FULL"].mean().astype(int))

        curr_date = curr_date+pd.DateOffset(weeks=1)

        week_d = week_d+pd.DateOffset(weeks=1)
                                                                                                
        if(week_d>=caphis.index[0]+pd.DateOffset(days=1)):
            break

    if curr_date<caphis.index[0]:

        week_d = caphis.index[0]

        st_l.append(curr_date)

        en_l.append(week_d)

        ch_l.append(caphis.loc[(caphis.index>=curr_date)&(caphis.index<=week_d)]["CHARGE_FULL"].mean().astype(int))
        
    caphistory["START_DATE"] = pd.Series(st_l)

    caphistory["END_DATE"] = pd.Series(en_l)

    caphistory["CHARGE_FULL (in mWh)"] = pd.Series(ch_l)

    caphistory["CHARGE_FULL_DESIGN (in mWh)"] = caphis["CHARGE_FULL_DESIGN"].iloc[0]

    return caphistory

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--html", action="store_true")

    parser.add_argument("--csv", action="store_true")

    parser.add_argument("--xml", action="store_true")

    parser.add_argument("--json", action="store_true")

    args = parser.parse_args()

    caphistory = capacity()

    caphistory["START_DATE"] = pd.to_datetime(caphistory["START_DATE"]).dt.strftime('%m/%d/%Y')

    caphistory["END_DATE"] = pd.to_datetime(caphistory["END_DATE"]).dt.strftime('%m/%d/%Y')

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
