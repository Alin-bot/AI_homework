import random

def get_initial_color_list(n:int, m:int, k:int)->list:
    color_list = []
    for i in range(0, n):
        for j in range(0, m):
            color_list.append(i)
    return random.sample(color_list, k)


def is_final_state(state:list, initial_state:list, round:int, n:int):
    if round > 2*n:
        return 'A'
    else:
        if state == initial_state:
            return 'B'
        else:
            return False


def choose_random_color_list(k:int, color_list:list):
    return random.sample(color_list, k)

def compare_sequences(state:list, goal_state:list)->int:
    difference = []
    for list1, list2 in zip(state, goal_state):
        difference.append(list1 - list2)
    return difference.count(0)
