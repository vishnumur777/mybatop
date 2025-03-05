import pandas as pd
import argparse
import json


def tech_specification():
    tech_spec = pd.read_csv("data.csv")

    tech_spec.dropna(subset=["SERIAL_NUMBER"], inplace=True)

    tech_spec = tech_spec[
        [
            "DATE",
            "TIME",
            "VOLTAGE_NOW",
            "CURRENT_NOW",
            "CHARGE_FULL",
            "CHARGE_NOW",
            "CAPACITY",
        ]
    ]

    tech_spec.head(5)

    tech_spec["DATE"] = pd.to_datetime(tech_spec["DATE"], format="%m/%d/%y")

    curr_date = tech_spec["DATE"].iloc[0]

    curr_date = pd.to_datetime(curr_date)

    th_bef = curr_date - pd.DateOffset(days=3)

    tech_spec["VOLTAGE_NOW"] = (tech_spec["VOLTAGE_NOW"] / 1000).astype(int)

    tech_spec["CURRENT_NOW"] = (tech_spec["CURRENT_NOW"] / 1000).astype(int)

    tech_spec["CHARGE_FULL"] = (tech_spec["CHARGE_FULL"] / 1000).astype(int)

    tech_spec["CHARGE_NOW"] = (tech_spec["CHARGE_NOW"] / 1000).astype(int)

    tech_spec1 = tech_spec.loc[
        (tech_spec["DATE"] > th_bef) & (tech_spec["DATE"] <= curr_date)
    ]

    tech_spec1.columns = [
        "DATE",
        "TIME",
        "VOLTAGE_NOW (in mWh)",
        "CURRENT_NOW (in mA)",
        "CHARGE_FULL (in mWh)",
        "CHARGE_NOW (in mWh)",
        "CAPACITY (%)",
    ]

    return tech_spec1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--html", action="store_true")

    parser.add_argument("--csv", action="store_true")

    parser.add_argument("--xml", action="store_true")

    parser.add_argument("--json", action="store_true")

    args = parser.parse_args()

    tech_spec = tech_specification()

    tech_spec["DATE"] = pd.to_datetime(tech_spec["DATE"]).dt.strftime("%m/%d/%Y")

    if args.html:
        tech_spec.to_html("b.html", index=False)

    elif args.csv:
        tech_spec.to_csv("index.csv", index=False)

    elif args.xml:
        tech_spec.columns = [
            "START_DATE",
            "END_DATE",
            "VOLTAGE_NOW",
            "CURRENT_NOW",
            "CHARGE_FULL",
            "CHARGE_NOW",
            "CAPACITY",
        ]
        tech_spec.to_xml("index.xml", index=False)

    elif args.json:
        records = tech_spec.to_dict(orient="records")
        pretty_json = json.dumps(records, indent=4)

        with open("index.json", "w") as f:
            f.write(pretty_json)
