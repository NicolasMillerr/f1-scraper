import pandas as pd
URL = (
    #"https://www.formula1.com/en/results.html/2020/races/1045/austria/race-result.html"
    "https://www.formula1.com/en/results.html/2020/races/1045/austria/qualifying.html"
)

import requests
from bs4 import BeautifulSoup


def make_f1_table_for_results(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "lxml")
    table = soup.find("table")
    rows = table.findAll("tr")

    all_rows = []
    for row in rows[1:]:
        columns = row.findAll("td")
        row_as_dict = {}
        for i, col in enumerate(columns):
            row_as_dict[i] = col.get_text()
        all_rows.append(row_as_dict)


    df = pd.DataFrame(all_rows)
    df[3] = df[3].apply(lambda x: x.replace("\n", " "))
    df = df.rename(columns ={
        1: "pos",
        2: "#",
        3: "driver",
        4: "team",
        5: "laps",
        6: "deltat",
        7: "points",

    })

    df= df[["pos",
    "#",
    "driver",
    "team",
    "laps",
    "deltat",
    "points",]]

    return df


# TODO: limpiar codigo repetido
def make_f1_table_for_quali(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "lxml")
    table = soup.find("table")
    rows = table.findAll("tr")

    all_rows = []
    for row in rows[1:]:
        columns = row.findAll("td")
        row_as_dict = {}
        for i, col in enumerate(columns):
            row_as_dict[i] = col.get_text()
        all_rows.append(row_as_dict)


    df = pd.DataFrame(all_rows)
    df[3] = df[3].apply(lambda x: x.replace("\n", " "))
    df = df.rename(columns ={
        1: "pos",
        2: "#",
        3: "driver",
        4: "team",
        5: "Q1",
        6: "Q2",
        7: "Q3",
        8: "Laps",

    })

    df= df[["pos",
    "#",
    "driver",
    "team",
    "Q1",
    "Q2",
    "Q3",
    "Laps",]]

    return df


"""
URLS = ["...."]
def func(URL):
    pass

for url in URLS:
    func(url)
"""
