import sys
import hashlib


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

    return state


def validate_transition(state: list, person_1: int = -1, person_2: int = -1) -> bool:

    if (
        state[person_1] != state[0]
        or state[person_2] != state[0]
        or state[person_1] != state[person_2]
    ):
        return False

    if state[0] == 1:

        state[0] = 2
    else:
        state[0] = 1

    for person in [person_1, person_2]:
        if not (person == -1) and person % 2 == 0:

            state[person] = state[0]

    protected = 0
    for person in [person_1, person_2]:
        if not (person == -1) and person % 2 == 1:
            if state[person + 1] == state[0]:

                protected = 1
            for male in range(2, len(state), 2):
                if state[male] == state[0] and protected == 0:

                    return False

    return True


def backtracking(state, visited_states, i, j):
    if is_final_state(state):
        print("Final state!")
        visited_states.append(hash_state(state))
        print(visited_states)
        return True
    # elif visited_state(state, visited_states):
    #     return False
    else:
        if not hash_state(state) in visited_states:
            visited_states.append(hash_state(state))
        for index_1 in range(1, len(state)):
            for index_2 in range(1, len(state)):
                state_copy = state.copy()
                if validate_transition(state_copy, index_1, index_2):
                    # print(f"State: {state}")
                    new_state = list(transition(state, index_1, index_2))
                    # print(f"New state: {new_state}")
                    if not hash_state(state) in visited_states:
                        backtracking(new_state, visited_states, index_1, index_2)
                        # print(state_copy, visited_states)
        visited_states.remove(visited_states[-1])


def hash_state(state):
    str_state = ""
    for i in state:
        str_state += str(i)
    # hash_state = hashlib.md5(str_state.encode()).hexdigest()
    return str_state


def visited_state(state: list, visited_states) -> bool:
    if hash_state(state) in visited_states:
        return True
    else:
        return False


def bkt_strategy(number_of_couples: int):
    state = get_initial_state(number_of_couples)

    return backtracking(state, [], 1, 1)

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
# print(validate_transition([1,1,1,1,1], 1, 4))           # female wants to get on the other side with another male and her husbant stays on the initial side (false)
# print(validate_transition([1,1,1,1,2], 1))              # female wants to get on the side where there is another male (false)

# sys.setrecursionlimit(5000)
# bkt_strategy(2)
