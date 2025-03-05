import pandas as pd

import plotly.express as px

import argparse

import json


def dcharecter():
    dchar = pd.read_csv("data.csv")

    dchar.dropna(subset=["SERIAL_NUMBER"], inplace=True)

    dchar = dchar[["DATE", "CAPACITY"]]

    dchar["DATE"] = pd.to_datetime(dchar["DATE"], format="%m/%d/%y")

    dchar["CAPACITY"] = dchar["CAPACITY"].astype(int)

    curr_date = dchar["DATE"].iloc[0]

    th_mon = curr_date - pd.DateOffset(months=1)

    tw = dchar.loc[(dchar["DATE"] >= th_mon) & (dchar["DATE"] <= curr_date)]

    tw1 = tw.groupby("DATE")["CAPACITY"].mean().reset_index()

    tw1["CAPACITY"] = tw1["CAPACITY"].round(2)

    return tw1


def generate_graph():
    df = dcharecter()

    figure = px.line(
        df, x="DATE", y="CAPACITY", markers=True, line_shape="spline", height=600
    )

    figure.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", font_color="white", font_family="Times New Roman"
    )

    figure.write_html("c.html")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--graph", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--html", action="store_true")
    parser.add_argument("--csv", action="store_true")
    parser.add_argument("--xml", action="store_true")

    args = parser.parse_args()

    if args.graph:
        generate_graph()
    elif args.html:
        df = dcharecter()
        df["DATE"] = pd.to_datetime(df["DATE"]).dt.strftime("%m/%d/%Y")
        df.to_html("Average_capacity.html")
    elif args.xml:
        df = dcharecter()
        df["DATE"] = pd.to_datetime(df["DATE"]).dt.strftime("%m/%d/%Y")
        df.to_html("Average_capacity.html")
    elif args.csv:
        df = dcharecter()
        df["DATE"] = pd.to_datetime(df["DATE"]).dt.strftime("%m/%d/%Y")
        df.to_html("Average_capacity.html")
    elif args.json:
        df = dcharecter()
        df["DATE"] = pd.to_datetime(df["DATE"]).dt.strftime("%m/%d/%Y")
        records = df.to_dict(orient="records")
        pretty_json = json.dumps(records, indent=4)

        with open("index.json", "w") as f:
            f.write(pretty_json)
