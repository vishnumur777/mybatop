import pandas as pd
import argparse
import json


def calculate_datetimedf(batuse):
    datetime_df = pd.DataFrame()

    datetime_df["START_DATE"] = batuse.groupby("GROUP").agg({"DATETIME": "first"})
    datetime_df["END_TIME"] = batuse.groupby("GROUP").agg({"DATETIME": "last"})
    datetime_df.reset_index(drop=True, inplace=True)

    return datetime_df


def battery_activity():
    batuse = pd.read_csv("batusageact.csv")

    batuse["DATETIME"] = pd.to_datetime(batuse["DATETIME"], format="%Y-%m-%d %H:%M:%S")

    datetime_df = calculate_datetimedf(batuse)

    batuse_ch = batuse[batuse["STATUS"] == "Charging"]
    batuse_dc = batuse[batuse["STATUS"] != "Charging"]

    batuse["DIFFERENCE"] = batuse["DATETIME"] - batuse.shift(-1)["DATETIME"]
    batuse["DIFFERENCE"] = batuse["DIFFERENCE"].fillna(pd.Timedelta(seconds=0))

    batuse_ch = batuse[batuse["STATUS"] == "Charging"]
    batuse_dc = batuse[batuse["STATUS"] != "Charging"]

    batuse_ch_act = batuse_ch[batuse_ch["STATE"] == "Active"]
    batuse_ch_low = batuse_ch[batuse_ch["STATE"] == "Low-Power"]

    batuse_dc_act = batuse_dc[batuse_dc["STATE"] == "Active"]
    batuse_dc_low = batuse_dc[batuse_dc["STATE"] == "Low-Power"]

    batuse_ch_act_gr = batuse_ch_act.groupby("GROUP")["DIFFERENCE"].sum().reset_index()
    batuse_ch_low_gr = batuse_ch_low.groupby("GROUP")["DIFFERENCE"].sum().reset_index()

    batuse_dc_act_gr = batuse_dc_act.groupby("GROUP")["DIFFERENCE"].sum().reset_index()
    batuse_dc_low_gr = batuse_dc_low.groupby("GROUP")["DIFFERENCE"].sum().reset_index()

    batuse_ch_act_gr = batuse_ch_act_gr.rename(
        columns={"DIFFERENCE": "CHARGING_ACTIVE"}
    )
    batuse_ch_low_gr = batuse_ch_low_gr.rename(
        columns={"DIFFERENCE": "CHARGING_LOW_POWER"}
    )
    batuse_dc_act_gr = batuse_dc_act_gr.rename(columns={"DIFFERENCE": "BATTERY_ACTIVE"})
    batuse_dc_low_gr = batuse_dc_low_gr.rename(
        columns={"DIFFERENCE": "BATTERY_LOW_POWER"}
    )

    df = (
        batuse_dc_act_gr.merge(batuse_dc_low_gr, on="GROUP", how="outer")
        .merge(batuse_ch_act_gr, on="GROUP", how="outer")
        .merge(batuse_ch_low_gr, on="GROUP", how="outer")
    )

    final_df = datetime_df.merge(df, on=datetime_df.index, how="outer")

    final_df = final_df.drop(columns=["key_0", "GROUP"])

    final_df = final_df.fillna("-")

    return final_df


def generate_html(final_df):
    table_header = """
    <table border="1">
        <thead>
            <tr class="header-row">
                <th rowspan="2">START_DATE</th>
                <th rowspan="2">END_DATE</th>
                <th colspan="2">ON_BATTERY</th>
                <th colspan="2">WHILE_CHARGING</th>
            </tr>
            <tr>
                <th>ACTIVE</th>
                <th>LOW_POWER</th>
                <th>ACTIVE</th>
                <th>LOW_POWER</th>
            </tr>
        </thead>
    """

    table_body = ""

    for i in range(len(final_df)):
        table_body += f"""
                <tr>
                    <td>{final_df["START_DATE"][i]}</td>
                    <td>{final_df["END_TIME"][i]}</td>
                    <td>{final_df["BATTERY_ACTIVE"][i]}</td>
                    <td>{final_df["BATTERY_LOW_POWER"][i]}</td>
                    <td>{final_df["CHARGING_ACTIVE"][i]}</td>
                    <td>{final_df["CHARGING_LOW_POWER"][i]}</td>
                </tr>
        """

    table_footer = """ 
        </tbody>
    </table>
    """

    full_table = table_header + table_body + table_footer

    with open("g.html", "w") as f:
        f.write(full_table)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--html", action="store_true")

    parser.add_argument("--csv", action="store_true")

    parser.add_argument("--xml", action="store_true")

    parser.add_argument("--json", action="store_true")

    args = parser.parse_args()

    final_df = battery_activity()

    if args.html:
        generate_html(final_df)

    elif args.csv:
        final_df.to_csv("battery_activity.csv", index=False)

    elif args.xml:
        final_df.to_xml("battery_activity.xml", index=False)

    elif args.json:
        records = final_df.to_dict(orient="records")
        pretty_json = json.dumps(records, indent=4)

        with open("index.json", "w") as f:
            f.write(pretty_json)
