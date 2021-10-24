import numpy as np
import pandas as pd
import random


def get_list_of_neighbours(countries: str):
    return countries.split(",")


def get_list_of_colors(colors: str):
    return colors.split(",")


def process_input(path: str):
    countries = pd.read_csv(path)
    countries["neighbours"] = countries["neighbours"].apply(
        lambda x: get_list_of_neighbours(x))
    countries["available_colors"] = countries["available_colors"].apply(
        lambda x: get_list_of_colors(x))
    countries["chosen_color"] = None
    return countries




