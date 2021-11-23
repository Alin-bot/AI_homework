from os import read
import pandas as pd
import math
import random


def read_input():
    boolean_function = pd.read_csv("input.csv")
    epochs = int(input("Enter the number of training epochs: "))
    learning_rate = float(input("Enter the learning rate: "))
    return {
        "boolean_function": boolean_function,
        "number_of_epochs": epochs,
        "learning_rate": learning_rate,
    }


def sigmoid_function(x):
    return math.exp(x) / (math.exp(x) + 1)


def predict_output(x1, x2):
    weight_1 = round(random.uniform(-1, 1), 2)
    weight_2 = round(random.uniform(-1, 1), 2)
    weight_3 = round(random.uniform(-1, 1), 2)
    weight_4 = round(random.uniform(-1, 1), 2)
    bias_1 = random.randrange(-10, 10)
    bias_2 = random.randrange(-10, 10)
    z_1 = weight_1 * x1 + weight_3 * x2 + bias_1
    z_2 = weight_2 * x1 + weight_4 * x2 + bias_2
    g_1 = sigmoid_function(z_1)
    g_2 = sigmoid_function(z_2)
    weight_5 = round(random.uniform(-1, 1), 2)
    weight_6 = round(random.uniform(-1, 1), 2)
    bias_3 = random.randrange(-10, 10)
    y_pred = weight_5 * g_1 + weight_6 * g_2 + bias_3
    return (
        y_pred,
        weight_1,
        weight_2,
        weight_3,
        weight_4,
        weight_5,
        weight_6,
        bias_1,
        bias_2,
        bias_3,
        z_1,
        z_2,
        g_1,
        g_2,
    )


def forward_propagation(df: pd.DataFrame):
    df["predicted_y"] = df.apply(lambda x: predict_output(x["X1"], x["X2"])[0], axis=1)
    df["weight_1"] = df.apply(lambda x: predict_output(x["X1"], x["X2"])[1], axis=1)
    df["weight_2"] = df.apply(lambda x: predict_output(x["X1"], x["X2"])[2], axis=1)
    df["weight_3"] = df.apply(lambda x: predict_output(x["X1"], x["X2"])[3], axis=1)
    df["weight_4"] = df.apply(lambda x: predict_output(x["X1"], x["X2"])[4], axis=1)
    df["weight_5"] = df.apply(lambda x: predict_output(x["X1"], x["X2"])[5], axis=1)
    df["weight_6"] = df.apply(lambda x: predict_output(x["X1"], x["X2"])[6], axis=1)
    df["bias_1"] = df.apply(lambda x: predict_output(x["X1"], x["X2"])[7], axis=1)
    df["bias_2"] = df.apply(lambda x: predict_output(x["X1"], x["X2"])[8], axis=1)
    df["bias_3"] = df.apply(lambda x: predict_output(x["X1"], x["X2"])[9], axis=1)
    df["z_1"] = df.apply(lambda x: predict_output(x["X1"], x["X2"])[10], axis=1)
    df["z_2"] = df.apply(lambda x: predict_output(x["X1"], x["X2"])[11], axis=1)
    df["g_1"] = df.apply(lambda x: predict_output(x["X1"], x["X2"])[12], axis=1)
    df["g_2"] = df.apply(lambda x: predict_output(x["X1"], x["X2"])[13], axis=1)

    return df


def compute_for_backward(df):

    df["cost"] = df.apply(lambda x: compute_cost(x["predicted_y"], x["Y"]), axis=1)
    df["deriv_cost_w5"] = df.apply(
        lambda x: compute_derivative_cost_w5(x["predicted_y"], x["Y"], x["g_1"]), axis=1
    )
    df["deriv_cost_w6"] = df.apply(
        lambda x: compute_derivative_cost_w6(x["predicted_y"], x["Y"], x["g_2"]), axis=1
    )
    df["deriv_cost_b3"] = df.apply(
        lambda x: compute_derivative_cost_b3(x["predicted_y"], x["Y"]), axis=1
    )
    learning_rate = read_input()["learning_rate"]
    df["weight_5"] = df.apply(
        lambda x: update_weight(x["weight_5"], learning_rate, x["deriv_cost_w5"]),
        axis=1,
    )
    df["weight_6"] = df.apply(
        lambda x: update_weight(x["weight_6"], learning_rate, x["deriv_cost_w6"]),
        axis=1,
    )
    print(df)


def compute_cost(y_pred, y_act):
    return (y_pred - y_act) ** 2


def compute_derivative_cost_w5(y_pred, y_act, g1):
    return 2 * (y_pred - y_act) * g1


def compute_derivative_cost_w6(y_pred, y_act, g2):
    return 2 * (y_pred - y_act) * g2


def compute_derivative_cost_b3(y_pred, y_act):
    return 2 * (y_pred - y_act)


def update_weight(weight, learning_rate, derivative):
    return weight - learning_rate * derivative


# print(read_input())
# print(sigmoid_function(1))
# print(forward_propagation(read_input()["boolean_function"]))
print(compute_for_backward(forward_propagation(read_input()["boolean_function"])))
