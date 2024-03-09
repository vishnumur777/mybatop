import pandas as pd


def activity():

    try:

        df = pd.read_csv("data.csv")

        batact = pd.DataFrame()

        fin_batact = pd.DataFrame()

        date_format = '%m/%d/%y %H:%M:%S'

        df["COMBINED_DT"] = pd.to_datetime(
            df["DATE"]+' '+df["TIME"], format=date_format)

        df["DATE"] = pd.to_datetime(df["DATE"], format="%m/%d/%y")

        curr_date = df["DATE"].iloc[-1]

        df["DATE"][0]

        rev_df = df[::-1].reset_index(drop=True)

        sus_loc = rev_df.loc[rev_df["STATUS"] == "Suspended"]

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

        if rev_df["STATUS"][0] == "Active":
            temp_act["DATE"] = pd.Series(rev_df["DATE"][0])

            temp_act["TIMESTAMP"] = pd.Series(pd.to_datetime(
                sus_loc["COMBINED_DT"][0]) - pd.to_datetime(rev_df["COMBINED_DT"][0]))

            batact["DATE"] = act_loc["DATE"]

            batact["TIMESTAMP"] = pd.to_datetime(
                act_loc["COMBINED_DT"]) - pd.to_datetime(sus_loc["COMBINED_DT"])

            batact = pd.concat([temp_act, batact], ignore_index=True)

        if rev_df["STATUS"][0] == "Suspended":

            batact["DATE"] = act_loc["DATE"]

            batact["TIMESTAMP"] = pd.to_datetime(
                act_loc["COMBINED_DT"]) - pd.to_datetime(sus_loc["COMBINED_DT"])

        curr_date = pd.to_datetime(df["DATE"].iloc[-1])

        week_d = curr_date+pd.DateOffset(weeks=1)

        st_l = []
        en_l = []
        ch_l = []

        while True:
            st_l.append(curr_date)

            en_l.append(week_d)

            ch_l.append(batact.loc[(batact["DATE"] >= curr_date) & (
                batact["DATE"] <= week_d)]["TIMESTAMP"].sum())

            curr_date = curr_date+pd.DateOffset(weeks=1)

            week_d = week_d+pd.DateOffset(weeks=1)

            if (week_d >= batact["DATE"].iloc[-1]+pd.DateOffset(days=1)):
                break

        if curr_date < batact["DATE"].iloc[-1]:

            week_d = batact["DATE"].iloc[-1]

            st_l.append(curr_date)

            en_l.append(week_d)

            ch_l.append(batact.loc[(batact["DATE"] >= curr_date) & (
                batact["DATE"] <= week_d)]["TIMESTAMP"].sum())

        fin_batact["START_DATE"] = pd.Series(st_l)

        fin_batact["END_DATE"] = pd.Series(en_l)

        fin_batact["TIME_USED"] = pd.Series(ch_l)

        fin_batact.to_html("e.html", index=False)

    except KeyError as e:

        if e == "0":

            print("No keys found")
