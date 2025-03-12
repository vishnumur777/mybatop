import pandas as pd
import plotly.express as px
import argparse
import json


def battery_health_df():
    df = pd.read_csv("/opt/mybatop/final.csv")

    df1 = df[["DATE"]].copy()

    df1["DATE"] = pd.to_datetime(df1["DATE"], format="%m/%d/%y")

    df1["BATTERY_HEALTH"] = round(df["CHARGE_FULL"] / df["CHARGE_FULL_DESIGN"] * 100, 2)

    df2 = df1.groupby(df1["DATE"])["BATTERY_HEALTH"].mean().reset_index()

    return df2


def plot_battery_health(df1):
    fig = px.line(df1, x="DATE", y="BATTERY_HEALTH", title="Battery Health Over Time")

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", font_color="white", font_family="Times New Roman"
    )

    fig.write_html("f.html")


if __name__ == "__main__":
    df = battery_health_df()

    parser = argparse.ArgumentParser()

    parser.add_argument("--graph", action="store_true")
    parser.add_argument("--html", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--csv", action="store_true")
    parser.add_argument("--xml", action="store_true")

    args = parser.parse_args()

    if args.graph:
        plot_battery_health(df)
    elif args.html:
        df["DATE"] = pd.to_datetime(df["DATE"]).dt.strftime("%d-%m-%Y")
        df.to_html("battery_health.html", index=False)
    elif args.csv:
        df["DATE"] = pd.to_datetime(df["DATE"]).dt.strftime("%d-%m-%Y")
        df.to_csv("battery_health.csv", index=False)
    elif args.xml:
        df["DATE"] = pd.to_datetime(df["DATE"]).dt.strftime("%d-%m-%Y")
        df.to_xml("battery_health.xml", index=False)
    elif args.json:
        df["DATE"] = pd.to_datetime(df["DATE"]).dt.strftime("%d-%m-%Y")
        records = df.to_dict(orient="records")
        pretty_json = json.dumps(records, indent=4)

        with open("battery_health.json", "w") as f:
            f.write(pretty_json)
