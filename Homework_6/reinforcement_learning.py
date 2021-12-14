import numpy as np
import random 

# -999 for ice, 1 for good path, 0 is initial state, 999 is final state

# actions: (0,1) - right, (0,-1) - left, (1,0) - down, (-1,0) - up

def initialize_environment(n: int, ice: int):

    Q = np.ones((n, n))
    Q[0,0] = 0
    Q[n-1,n-1] = 999

    while ice > 0:
        first_pos = random.randint(0,n-1)
        second_pos = random.randint(0,n-1)

        if (first_pos == 0 and second_pos == 0) or (second_pos == (n-1) and first_pos == (n-1)):
            continue

        if Q[first_pos,second_pos] != -999:
            ice -= 1
            Q[first_pos,second_pos] = -999

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
    agent = np.where(matrix == 0)
    # print('\n', agent, '\n')
    row_agent = agent[0][0]
    col_agent = agent[1][0]
    return (row_agent, col_agent)


def action(matrix, move: tuple):
    agent = find_agent(matrix)

    if validate_action(matrix, move, agent):
        if matrix[agent[0] + move[0], agent[1] + move[1]] == -999:
            print("You lost!")
            return 0
        elif matrix[agent[0] + move[0], agent[1] + move[1]] == 999:
            print("You won!")
            return 1

        matrix[agent[0] + move[0], agent[1] + move[1]] = 0
        matrix[agent[0], agent[1]] = 1

    else:
        print("Incorrect move!")
        return 0

def get_next_action(Q, agent: tuple, epsilon):
    if np.random.random() < epsilon:
        max_value = np.argmax(Q[agent[0], agent[1]])
        location = np.where(Q == max_value)
        row = location[0][0]
        col = location[1][0]
        return (row, col)
    else:
        random_move = np.random.randint(4)
        if random_move == 1:
            return (0,1)
        if random_move == 2:
            return (0,-1)
        if random_move == 3:
            return (1,0)
        if random_move == 4:
            return (-1,0)

def Q_learning():
    n = int(input("Enter the matrix size: "))
    ice = int(input("Enter the thin ice number: "))
    epsilon = 0.9
    discount_factor = 0.9
    learning_rate = 0.9

    rewards = np.full((n, n), -999.)
    rewards[0, 0] = 0
    rewards[n-1, n-1] = 999

    for episode in range(100):
        Q = initialize_environment(n, ice)

        move = get_next_action(Q, find_agent(Q), epsilon)
        print(move)
        print(Q)
        while not action(Q, move):

            print(Q)
            agent_location = find_agent(Q)
            reward = rewards[agent_location[0], agent_location[1]]
            
            move[0] -= agent_location[0]
            move[1] -= agent_location[1]

            old_q_value = Q[move[0], move[1]]
            temporal_difference = reward + (discount_factor * np.max(Q[agent_location[0], agent_location[1]])) - old_q_value

            new_q_value = old_q_value + (learning_rate * temporal_difference)
            Q[move[0], move[1]] = new_q_value

            move = get_next_action(Q, find_agent(Q), epsilon)
    
    print('Training compltete!')


Q_learning()