import numpy as np
import random 

# -1 for ice, 0 for good path, 1 is initial state, 2 is final state

# actions: (0,1) - right, (0,-1) - left, (1,0) - down, (-1,0) - up

def initialize_environment(n: int, ice: int):

    Q = np.zeros((n, n))
    Q[0,0] = 1
    Q[n-1,n-1] = 2

    while ice > 0:
        first_pos = random.randint(0,n-1)
        second_pos = random.randint(0,n-1)

        if (first_pos == 0 and second_pos == 0) or (second_pos == (n-1) and first_pos == (n-1)):
            continue

        if Q[first_pos,second_pos] != -1:
            ice -= 1
            Q[first_pos,second_pos] = -1

    return Q

def validate_action(matrix, move: tuple, agent: tuple):
    if (agent[0] == (len(matrix) - 1)) and (move[0] == 1):
            return False

    if (agent[1] == (len(matrix) - 1)) and (move[1] == 1):
            return False

    if (agent[0] == 0) and (move[0] == -1):
            return False

    if (agent[1] == 0) and (move[1] == -1):
            return False

    return True

def find_agent(matrix):
    agent = np.where(matrix == 1)
    row_agent = agent[0][0]
    col_agent = agent[1][0]
    return (row_agent, col_agent)


def action(matrix, move: tuple):
    agent = find_agent(matrix)

    if validate_action(matrix, move, agent):
        if matrix[agent[0] + move[0], agent[1] + move[1]] == -1:
            print("You lost!")
            return -1
        elif matrix[agent[0] + move[0], agent[1] + move[1]] == 2:
            print("You won!")
            return 0

        matrix[agent[0] + move[0], agent[1] + move[1]] = 1
        matrix[agent[0], agent[1]] = 0

    else:
        print("Incorrect move!")
        return -1


def reinforcement_learning():
    n = int(input("Enter the matrix size: "))
    ice = int(input("Enter the thin ice number: "))

    Q = initialize_environment(n, ice)

    print("matrix before action:")
    print(Q)

    action(Q, (0,1))

    print("matrix after:")
    print(Q)

reinforcement_learning()