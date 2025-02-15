import pandas as pd
import argparse
import json
def activity():

    try:

        df = pd.read_csv("data.csv")

        batact = pd.DataFrame()

        fin_batact = pd.DataFrame()

        date_format = '%m/%d/%y %H:%M:%S'

        df["COMBINED_DT"] = pd.to_datetime(df["DATE"]+' '+df["TIME"], format=date_format)

        df["DATE"] = pd.to_datetime(df["DATE"], format="%m/%d/%y")

        curr_date = df["DATE"].iloc[-1]

        rev_df = df[::-1].reset_index(drop=True)

        sus_loc = rev_df.loc[rev_df["STATE"] == "Suspended"]

        act_ind = sus_loc.index+1

        act_loc = rev_df.loc[act_ind]

        sus_loc = sus_loc.reset_index(drop=True)

        act_loc = act_loc.reset_index(drop=True)

        def format_timedelta(timedelta_object):

            days = timedelta_object.days

            seconds = timedelta_object.seconds

            hours, remainder = divmod(seconds, 3600)

            minutes, seconds = divmod(remainder, 60)

            return f"{24 * days + hours:02d}:{minutes:02d}:{seconds:02d}"

        temp_act = pd.DataFrame()

        if rev_df["STATE"][0] == "Active":
            
            temp_act["DATE"] = pd.Series(rev_df["DATE"].iloc[0])

            temp_act["TIMESTAMP"] = pd.Series(pd.to_datetime(sus_loc["COMBINED_DT"][0]) - pd.to_datetime(rev_df["COMBINED_DT"][0]))

            batact["DATE"] = act_loc["DATE"]

            batact["TIMESTAMP"] = pd.to_datetime(act_loc["COMBINED_DT"]) - pd.to_datetime(sus_loc["COMBINED_DT"])

            batact = pd.concat([temp_act, batact], ignore_index=True)

        if rev_df["STATE"][0] == "Suspended":

            batact["DATE"] = act_loc["DATE"]

            batact["TIMESTAMP"] = pd.to_datetime(act_loc["COMBINED_DT"]) - pd.to_datetime(sus_loc["COMBINED_DT"])

        curr_date = pd.to_datetime(df["DATE"].iloc[-1])

        week_d = curr_date+pd.DateOffset(weeks=1)

        st_l = []
        en_l = []
        ch_l = []

        while True:
            st_l.append(curr_date)

            en_l.append(week_d)

            ch_l.append(batact.loc[(batact["DATE"] >= curr_date) & (batact["DATE"] <= week_d)]["TIMESTAMP"].sum())

            curr_date = curr_date+pd.DateOffset(weeks=1)

            week_d = week_d+pd.DateOffset(weeks=1)

            if (week_d >= batact["DATE"].iloc[-1]+pd.DateOffset(days=1)):
                break

        if curr_date < batact["DATE"].iloc[-1]:

            week_d = batact["DATE"].iloc[-1]

            st_l.append(curr_date)

            en_l.append(week_d)

            ch_l.append(batact.loc[(batact["DATE"] >= curr_date) & (batact["DATE"] <= week_d)]["TIMESTAMP"].sum())

        fin_batact["START_DATE"] = pd.Series(st_l)

        fin_batact["END_DATE"] = pd.Series(en_l)

        fin_batact["TIME_USED"] = pd.Series(ch_l).apply(format_timedelta)

        return fin_batact

    except KeyError as e:

        if e == "0":

            print("No keys found")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--html", action="store_true")

    parser.add_argument("--csv", action="store_true")

    parser.add_argument("--xml", action="store_true")

    parser.add_argument("--json", action="store_true")

    args = parser.parse_args()

    activity = activity()

    activity["START_DATE"] = pd.to_datetime(activity["START_DATE"]).dt.strftime('%m/%d/%Y')

    activity["END_DATE"] = pd.to_datetime(activity["END_DATE"]).dt.strftime('%m/%d/%Y')

    if args.html:

        activity.to_html("e.html",index=False)

    elif args.csv:

        activity.to_csv("index.csv",index=False)

    elif args.xml:

        activity.to_xml("index.xml",index=False)

    elif args.json:

        records = activity.to_dict(orient='records')
        pretty_json = json.dumps(records, indent=4)

        with open('index.json', 'w') as f:
            f.write(pretty_json)