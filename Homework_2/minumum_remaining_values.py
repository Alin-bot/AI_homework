import pandas as pd
import numpy as np
from model import process_input
import random


def heuristic_function(df, country_id: str):
    available_colors = df[df['country_id'] ==
                          country_id]["available_colors"].values[0]
    return len(available_colors)


def compute_score_of_available_country(df):
    df['score'] = None
    for index, row in df.iterrows():
        if df.loc[index]['chosen_color'] is None:
            df.loc[index]['score'] = heuristic_function(df, row['country_id'])
    return df


def mrv(filename: str):
    countries = process_input(filename)
    countries = compute_score_of_available_country(countries)
    while not countries["score"].isnull().all():
        countries = countries.sort_values(by=["score"], ascending=True)
        print(countries)
        first = countries.head(1)
        available_colors = first["available_colors"].values[0]
        print(available_colors)
        chosen_color = random.choice(available_colors)
        print(chosen_color)
        first["chosen_color"] = chosen_color
        print(first["country_id"].values[0])
        for index, row in countries.iterrows():
            if first["country_id"].values[0] in countries.loc[index]["neighbours"] and chosen_color in countries.loc[index]["available_colors"]:
                countries.loc[index]["available_colors"].remove(chosen_color)
        countries = compute_score_of_available_country(countries)


mrv("example_2.csv")
