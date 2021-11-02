import random


def get_initial_color_list(n: int, m: int, k: int) -> list:
    color_list = []
    for i in range(0, n):
        for j in range(0, m):
            color_list.append(i)
    return random.sample(color_list, k)


def is_final_state(state: list, initial_state: list, round: int, n: int):
    if round >= 2 * n:
        return "A"
    else:
        if state == initial_state:
            return "B"
        else:
            return False


def choose_random_color_list(k: int, color_list: list):
    return random.sample(color_list, k)


def compare_sequences(state: list, goal_state: list) -> int:
    difference = []
    for list1, list2 in zip(state, goal_state):
        difference.append(list1 - list2)
    return difference.count(0)


def play_game(initial_state: list, n: int, m: int):
    turn = 0
    available_colors = [color for color in range(m)]
    while True:
        turn += 1
        print(f"---Round {turn}---")
        print(
            f"Input a combination of {len(initial_state)} balls from {available_colors}"
        )
        string_input = input()
        round_list = string_input.split(" ")
        round_list = [int(ball) for ball in round_list]
        print(compare_sequences(round_list, initial_state))
        if is_final_state(round_list, initial_state, turn, n) == "A":
            print("Player A won!")
            break
        else:
            if is_final_state(round_list, initial_state, turn, n) == "B":
                print(f"Player B won! Initial combination was {initial_state}")
                break


play_game(get_initial_color_list(3, 3, 4), 3, 3)
