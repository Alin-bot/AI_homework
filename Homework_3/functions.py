import random
import itertools


def get_initial_color_list(n: int, m: int) -> list:
    color_list = []
    for i in range(0, n):
        for j in range(0, m):
            color_list.append(i)
    return color_list


def is_final_state(state: list, initial_state: list, round: int, n: int):
    if round >= 2 * n:
        return "A"
    else:
        if state == initial_state:
            return "B"
        else:
            return False


def choose_goal_list(k: int, color_list: list):
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
        print(f"---Round {turn}/{2*n}---")
        print(
            f"Input a combination of {len(initial_state)} balls from {available_colors}"
        )
        string_input = input()
        round_list = string_input.split(" ")
        round_list = [int(ball) for ball in round_list]
        print(f"You have guessed {compare_sequences(round_list, initial_state)} balls!")
        if is_final_state(round_list, initial_state, turn, n) == "A":
            print("Player A won!")
            break
        else:
            if is_final_state(round_list, initial_state, turn, n) == "B":
                print(f"Player B won! Initial combination was {initial_state}")
                break


# play_game(get_initial_color_list(3, 3, 4), 3, 3)


def minimax_alphabeta(
    initial_state, depth: int, state: list, alpha, beta, turn, n, m, k, count
):
    balls = get_initial_color_list(n, m)
    print(balls)
    print(initial_state)
    if is_final_state(state, initial_state, turn, n) != False or depth == 0:
        return compare_sequences(state, initial_state)
    else:
        print(list(itertools.permutations(balls, k)))
        for choice in list(itertools.permutations(balls, k)):
            choice = list(choice)
            score = minimax_alphabeta(
                initial_state,
                depth - 1,
                choice,
                alpha,
                beta,
                turn + 1,
                n,
                m,
                k,
                count + 1,
            )
            if score >= beta:
                print(count)
                return beta
            if score > alpha:
                alpha = score


minimax_alphabeta(
    choose_goal_list(2, get_initial_color_list(2, 3)),
    2,
    [],
    -1000,
    -1000,
    0,
    2,
    3,
    2,
    0,
)
