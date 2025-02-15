import pandas as pd

import plotly.express as px

def dcharecter():

    dchar = pd.read_csv("data.csv")

    dchar.dropna(subset=["SERIAL_NUMBER"],inplace=True)

    dchar = dchar[["DATE","CAPACITY"]]

    dchar["DATE"] = pd.to_datetime(dchar["DATE"],format='%m/%d/%y')

    dchar["CAPACITY"] = dchar["CAPACITY"].astype(int)

    curr_date = dchar["DATE"].iloc[0]

    th_mon = curr_date - pd.DateOffset(months=1)

    tw = dchar.loc[(dchar["DATE"]>=th_mon) & (dchar["DATE"]<=curr_date)]

    tw1 = tw.groupby("DATE")["CAPACITY"].mean().reset_index()

    tw1["CAPACITY"] = tw1["CAPACITY"].round(2)

    return tw1

def generate_graph():

    df = dcharecter()

    figure = px.line(df,x="DATE",y="CAPACITY",markers=True,line_shape="spline",height=600)

    figure.update_layout(paper_bgcolor= 'rgba(0,0,0,0)',font_color="white",font_family="Times New Roman")

    figure.write_html("c.html")