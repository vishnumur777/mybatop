import pandas as pd
import argparse
import json


# getting recent 3 days format
def analyse():
    df = pd.DataFrame()

    try:
        df = pd.read_csv("data.csv")

    except pd.errors.ParserError:
        print("DataFrame elements are out of bound than the given column.")

    df.dropna(subset=["SERIAL_NUMBER"], inplace=True)

    yt = df.drop(
        columns=[
            "TECHNOLOGY",
            "NAME",
            "DEVTYPE",
            "SOURCE",
            "CYCLE_COUNT",
            "PRESENT",
            "MODEL_NAME",
            "MANUFACTURER",
            "SERIAL_NUMBER",
            "VOLTAGE_MIN_DESIGN",
            "VOLTAGE_NOW",
            "CURRENT_NOW",
            "CHARGE_FULL_DESIGN",
            "CHARGE_FULL",
            "CHARGE_NOW",
            "CAPACITY_LEVEL",
        ]
    )

    yt["DATE"] = pd.to_datetime(yt["DATE"], format="%m/%d/%y")

    curr_date = yt["DATE"].iloc[0]

    curr_date = pd.to_datetime(curr_date)

    th_bef = curr_date - pd.DateOffset(days=3)

    filtered_yt = yt.loc[(yt["DATE"] > th_bef) & (yt["DATE"] <= curr_date)]

    filtered_yt = filtered_yt.reset_index(drop=True)

    return filtered_yt


def conv_html(output):
    df = analyse()

    html_rows = []

    for i, rows in df.iterrows():
        if i == 0:
            html_rows.append("<tr>")

            for h in df.columns:
                html_rows.append(f"<th>{h}</th>")

            html_rows.append("</tr>")

        status_class = "recent-usage-status" if rows["STATE"] is not None else ""

        status_class1 = "recent-status" if rows["STATUS"] is not None else ""

        formatted_date = rows.DATE.strftime("%d-%m-%Y")

        html_row = f"<tr><td>{formatted_date}</td><td>{rows.TIME}</td><td class={status_class}>{rows.STATE}</td><td class={status_class1}>{rows.STATUS}</td><td>{rows.CAPACITY}</td></tr>"

        html_rows.append(html_row)

    html_table = (
        '<div class="recent-usage-table"><table border="1">'
        + "\n".join(html_rows)
        + "</table></div>"
    )

    with open(output, "w") as f:
        f.write(html_table)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--html", action="store_true")

    parser.add_argument("--csv", action="store_true")

    parser.add_argument("--xml", action="store_true")

    parser.add_argument("--json", action="store_true")

    args = parser.parse_args()

    activity = analyse()

    activity["DATE"] = pd.to_datetime(activity["DATE"]).dt.strftime("%Y/%m/%d")
        
    if args.html:
        conv_html("a.html")

    elif args.csv:
        activity.to_csv("recent_usage.csv", index=False)

    elif args.xml:
        activity.to_xml(".temp_xml_files/recent_usage.xml", index=False)

    elif args.json:
        records = activity.to_dict(orient="records")
        pretty_json = json.dumps(records, indent=4)

        with open(".temp_json_files/recent_usage.json", "w") as f:
            f.write(pretty_json)
