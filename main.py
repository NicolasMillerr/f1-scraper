import pandas as pd
import requests
from bs4 import BeautifulSoup

URLS = {
    "results": "https://www.formula1.com/en/results.html/2020/races/1045/austria/race-result.html",
    "quali": "https://www.formula1.com/en/results.html/2020/races/1045/austria/qualifying.html"
}

# TODO: inferir columnas desde row 1 de tabla html
RESULTS_COLUMNS = {
        1: "pos",
        2: "#",
        3: "driver",
        4: "team",
        5: "laps",
        6: "deltat",
        7: "points",
    }
QUALI_COLUMNS = {
        1: "pos",
        2: "#",
        3: "driver",
        4: "team",
        5: "Q1",
        6: "Q2",
        7: "Q3",
        8: "Laps",
    }

def get_soup_from_url(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "lxml")
    return soup

def get_table_rows_from_soup(soup):
    table = soup.find("table")
    table_rows = table.findAll("tr")
    all_rows = []
    for row in table_rows[1:]:
        columns = row.findAll("td")
        row_as_dict = {}
        for i, col in enumerate(columns):
            row_as_dict[i] = col.get_text()
        all_rows.append(row_as_dict)
    return all_rows

def make_datafarme_from_table(table, columns_dict):
    df = pd.DataFrame(table)
    df[3] = df[3].apply(lambda x: x.replace("\n", " "))

    df = df.rename(columns = columns_dict)
    keys = [value for _, value in columns_dict.items()]

    df= df[keys]

    return df

"""
URLS = ["...."]
def func(URL):
    pass

for url in URLS:
    func(url)
"""
