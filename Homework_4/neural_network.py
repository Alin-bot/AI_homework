import pandas as pd
import math


def read_input():
    boolean_function = pd.read_csv("Homework_4/input.csv")
    epochs = int(input("Enter the number of training epochs: "))
    learning_rate = float(input("Enter the learning rate: "))
    return {
        "boolean_function": boolean_function,
        "number_of_epochs": epochs,
        "learning_rate": learning_rate,
    }


def sigmoid_function(x):
    return math.exp(x) / (math.exp(x) + 1)


print(read_input())
print(sigmoid_function(1))
