import pandas as pd


def get_details():
    df = pd.read_csv("details.csv")

    length = df.shape[-1]

    user = '<div class="container">'

    user += '<div><h3 class="title">Laptop details</h3></div>'

    user += '<div class="battery-details">'

    for i in range(5):
        user += f'<div class="battery-content"><h3>{df.columns[i]}</h3><p>{df.values[0][i]}</p></div>'

    user += "</div>"

    user += '<div class="container">'

    user += '<div><h3 class="title"> Battery details</h3></div>'

    user += '<div class="battery-details">'

    for i in range(5, length):
        user += f'<div class="battery-content"><h3>{df.columns[i]}</h3><p>{df.values[0][i]}</p></div>'

    user += "</div>"

    with open("a0.html", "w") as f:
        f.write(user)


if __name__ == "__main__":
    get_details()
