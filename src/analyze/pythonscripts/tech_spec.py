import pandas as pd

def tech_specification():

    tech_spec = pd.read_csv("data.csv")

    tech_spec.dropna(subset=["SERIAL_NUMBER"],inplace=True)

    tech_spec = tech_spec[["DATE","TIME","VOLTAGE_NOW","CURRENT_NOW","CHARGE_FULL","CHARGE_NOW","CAPACITY"]]

    tech_spec.head(5)

    tech_spec["DATE"] = pd.to_datetime(tech_spec["DATE"],format='%m/%d/%y')

    curr_date=tech_spec["DATE"].iloc[0]

    curr_date=pd.to_datetime(curr_date)

    th_bef = curr_date - pd.DateOffset(days=3)

    tech_spec["VOLTAGE_NOW"] = (tech_spec["VOLTAGE_NOW"]/1000).astype(int)

    tech_spec["CURRENT_NOW"] = (tech_spec["CURRENT_NOW"]/1000).astype(int)

    tech_spec["CHARGE_FULL"] = (tech_spec["CHARGE_FULL"]/1000).astype(int)

    tech_spec["CHARGE_NOW"] = (tech_spec["CHARGE_NOW"]/1000).astype(int)

    tech_spec1 = tech_spec.loc[(tech_spec["DATE"]>th_bef) & (tech_spec["DATE"]<=curr_date)]

    tech_spec1.columns = ["DATE","TIME","VOLTAGE_NOW (in mWh)","CURRENT_NOW (in mA)","CHARGE_FULL (in mWh)","CHARGE_NOW (in mWh)","CAPACITY (%)"]

    tech_spec1.to_html("b.html",index=False)