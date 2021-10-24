from model import process_input
import random


def forward_checking(filename: str):
    countries = process_input(filename)
    for index, row in countries.iterrows():
        if countries.loc[index]["chosen_color"] is None:
            available_colors = countries.loc[index]["available_colors"]
            if available_colors == []:
                countries.to_csv("output.csv")
                raise Exception("There are no available colors left for ", countries.loc[index]['country_id'])
            assigned_color = random.choice(available_colors)
            countries.loc[index]["chosen_color"] = assigned_color
            for index_2, row_2 in countries.iterrows():
                if row["country_id"] in countries.loc[index_2]["neighbours"] and row["chosen_color"] in countries.loc[index_2]["available_colors"]:
                    countries.loc[index_2]["available_colors"].remove(
                        row["chosen_color"])
            partial_solution = countries.copy(deep=True)
            print(partial_solution)
        countries.to_csv("output.csv")


if __name__ == "__main__":
    forward_checking("example_1.csv")
