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
        elif agent[0] + move[0] == len(matrix) and agent[1] + move[1] == len(matrix):
            print("You won!")
            return 1

        matrix[agent[0] + move[0], agent[1] + move[1]] = 0
        matrix[agent[0], agent[1]] = 1

    else:
        print("Incorrect move!")
        return 0

def get_next_action(Q, agent: tuple, epsilon):
    if np.random.random() < epsilon:
        if validate_action(Q, (0, -1), agent):
            left = Q[agent[0], agent[1] - 1]
        else:
            left = -1000
        if validate_action(Q, (0, 1), agent):
            right = Q[agent[0], agent[1] + 1]
        else:
            right = -1000
        if validate_action(Q, (-1, 0), agent):
            up = Q[agent[0] - 1, agent[1]]
        else:
            up = -1000
        if validate_action(Q, (1, 0), agent):
            down = Q[agent[0] + 1, agent[1]]
        else:
            down = -1000

        max_value = np.argmax([right, down, left, up])
        
        max_value += 1
        if max_value == 1:
            return (0, 1)
        if max_value == 2:
            return (1, 0)
        if max_value == 3:
            return (0, -1)
        if max_value == 4:
            return (-1, 0)
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

    q_values = np.zeros((n, n, 4))
    

    for episode in range(100):
        Q = initialize_environment(n, ice)

        move = get_next_action(Q, find_agent(Q), epsilon)
        print(move)
        print(Q, '\n')
        while not action(Q, move):

            print(Q, '\n')
            agent = find_agent(Q)
            reward = rewards[agent[0], agent[1]]
            
            old_row_index = move[0] - agent[0]
            old_column_index = move[1] - agent[1]

            old_q_value = Q[old_row_index, old_column_index]
            
            if validate_action(Q, (0, -1), agent):
                left = Q[agent[0], agent[1] - 1]
            else:
                left = -1000
            if validate_action(Q, (0, 1), agent):
                right = Q[agent[0], agent[1] + 1]
            else:
                right = -1000
            if validate_action(Q, (-1, 0), agent):
                up = Q[agent[0] - 1, agent[1]]
            else:
                up = -1000
            if validate_action(Q, (1, 0), agent):
                down = Q[agent[0] + 1, agent[1]]
            else:
                down = -1000

            temporal_difference = reward + (discount_factor * np.max([left, down, up, right])) - old_q_value

            new_q_value = old_q_value + (learning_rate * temporal_difference)
            Q[old_row_index, old_column_index] = new_q_value

            move = get_next_action(Q, find_agent(Q), epsilon)
    
    print('Training compltete!')

# Q = initialize_environment(4,3)
# print(get_next_action(Q, (0,0), 0.9))

Q_learning()