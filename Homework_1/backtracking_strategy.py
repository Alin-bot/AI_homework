from jealous_husbands import *


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
