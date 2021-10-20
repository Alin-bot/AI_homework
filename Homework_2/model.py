from numpy import NaN
import pandas as pd

countries = pd.read_csv("countries.csv")


def get_list_of_neighbours(countries: str):
    return countries.split(",")


def get_list_of_colors(colors: str):
    return colors.split(",")


print(countries)
