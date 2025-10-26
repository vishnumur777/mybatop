import pandas as pd
import argparse
import plotly.express as px
import json


def cycle_count_df():
    df = pd.read_csv("data.csv")

    df["DATE"] = pd.to_datetime(df["DATE"], format="%m/%d/%y")

    df1 = df.groupby(df["DATE"])["CYCLE_COUNT"].mean().reset_index()

    df1["CYCLE_COUNT"] = df1["CYCLE_COUNT"].astype(int)

    df["DATE"] = df["DATE"].dt.strftime("%d-%m-%Y")

    return df1


def plot_cycle_count(df1):
    fig = px.line(df1, x="DATE", y="CYCLE_COUNT", title="Cycle Count Over Time")

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", font_color="white", font_family="Times New Roman"
    )

    fig.write_html("g.html")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--graph", action="store_true")
    parser.add_argument("--html", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--csv", action="store_true")
    parser.add_argument("--xml", action="store_true")

    args = parser.parse_args()

    df = cycle_count_df()

    if args.graph:
        plot_cycle_count(df)

    elif args.html:
        df.to_html("cycle_count.html", index=False)

    elif args.csv:
        df.to_csv("cycle_count.csv", index=False)

    elif args.xml:
        df.to_xml(".temp_xml_files/cycle_count.xml", index=False)

    elif args.json:
        df["DATE"] = df["DATE"].dt.strftime("%d-%m-%Y")
        records = df.to_dict(orient="records")
        pretty_json = json.dumps(records, indent=4)

        with open(".temp_json_files/cycle_counts.json", "w") as f:
            f.write(pretty_json)
