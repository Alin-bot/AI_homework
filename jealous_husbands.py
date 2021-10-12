import sys
import hashlib
from copy import deepcopy


def get_initial_state(number_of_couples: int):

    initial_state = [1] * (1 + number_of_couples * 2)
    return initial_state


def is_final_state(state: list) -> bool:

    return all(element == 2 for element in state) and (len(state) % 2 == 1)


def transition(state: list, person_1: int = -1, person_2: int = -1) -> list:
    if state[0] == 1:

        state[0] = 2
    else:
        state[0] = 1

    for person in [person_1, person_2]:
        if not person == -1:

            state[person] = state[0]

    return [transition for transition in state]


def validate_transition(state: list, person_1: int = -1, person_2: int = -1) -> bool:

    if state[0] == 1:

        state[0] = 2
    else:
        state[0] = 1

    for person in [person_1, person_2]:
        if not person == -1 and person % 2 == 0:

            state[person] = state[0]

    protected = 0
    for person in [person_1, person_2]:
        if not person == -1 and person % 2 == 1:
            if state[person+1] == state[0]:

                protected = 1
            for male in range(2, len(state), 2):
                if state[male] == state[0] and protected == 0:

                    return False

    return True


def backtraking(state, visited_states, i, j):
    ppl = []
    for i in range(1, len(state)):
        if state[i] == state[0]:
            ppl.append(i)
    ppl.append(-1)
    # print(ppl)

    if is_final_state(state):
        return True
    elif visited_state(state, visited_states):
        return False
    else:
        visited_states.append(state)
        # print(visited_states)
        # for index_1 in range(i, len(ppl)):
        #     for index_2 in range(j, len(ppl)):
                # print(index_1, index_2)
        state_2 = state.copy()
        if validate_transition(state_2, 3, 4):
            new_state = list(transition(state, 3, 4))
            print(new_state)
            # print(transition(state, 3, 4))
            # backtraking(new_state, visited_states, index_1, index_2)


def hash_state(state):
    str_state = ""
    for i in state:
        str_state += str(i)
    hash_state = hashlib.md5(str_state.encode()).hexdigest()
    return hash_state


def visited_state(state: list, visited_states) -> bool:
    if hash_state(state) in visited_states:
        return True
    else:
        return False


def bkt_strategy(number_of_couples: int):
    state = get_initial_state(number_of_couples)

    # id_couple = 1
    # while not is_final_state(state):

    #     id_couple = id_couple + 1
    #     choose_function(state, id_couple)
    #     if validate_transition(state):

    #         state = transition(state)

    return backtraking(state)
    # else:
    #     for i in ppl:
    #         for j in ppl:
    #             if validate_transition(state, i, j):
    #                 backtraking(transition(state, i, j))
    # if is_final_state(state):

    #     return True
    # elif not validate_transition(state):

    #     return False
    # else:
    #     for i in range(1, len(state)):
    #         for j in range(1, len(state)):
    #             backtraking(transition(state, male_ =  , female_ = ))


    # TESTING FUNCTIONS
# print(get_initial_state(5))             # should print inistial state list
# print(is_final_state([2, 1, 2, 2, 2]))  # should print False
# print(is_final_state([2, 2, 2, 2]))     # should print False
# print(is_final_state([2, 2, 2, 2, 2]))  # should print True
# print(transition(get_initial_state(5), 2, 6))
# print(transition(get_initial_state(5), 2, 1))
# print(transition([1, 1, 2, 1, 1], 4, 1))
# print(transition([2, 1, 2, 2, 2], 3))
# print(validate_transition(get_initial_state(5), 2, 1))  # true
# print(validate_transition([1,1,2,1,1], 4, 1))           # husband is on the future side and the female wants to get on the side with another male (true)
# print(validate_transition([1,1,1,1,1], 4, 1))           # female wants to get on the other side with another male and her husbant stays on the initial side (false)
# print(validate_transition([1,1,1,1,2], 1))              # female wants to get on the side where there is another male (false)
sys.setrecursionlimit(5000)
backtraking(get_initial_state(2), [], 1, 2)
# print(hash_state([1, 2, 1, 2, 1]))
