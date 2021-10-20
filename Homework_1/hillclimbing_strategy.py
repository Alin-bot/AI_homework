from jealous_husbands import is_final_state, get_initial_state, validate_transition
import random


def heuristic_function(state: list) -> int:
    nr = 0
    for i in range(1, len(state)):
        if state[i] == 2:
            nr += 1
    return nr


def is_wife_without_husband_and_not_single(state, wife_index):
    if state[wife_index] == state[wife_index + 1]:
        return False
    else:
        for i in range(2, len(state), 2):
            if state[wife_index] == state[i]:
                return True
    return False


def validate_wives(state):
    for i in range(1, len(state), 2):
        if is_wife_without_husband_and_not_single(state, i):
            return False
    return True


def validate_new_state(old_state, new_state) -> bool:
    if new_state == []:
        return False

    # The boat didn't move
    if old_state[0] == new_state[0]:
        return False

    difference = []
    for list1, list2 in zip(old_state, new_state):
        difference.append(list1 - list2)
    difference.pop(0)  # remove the boat

    # if there are move from side 1 and 2
    if difference.count(1) == difference.count(-1):
        return False

    # if there are too many moves
    if difference.count(1) > 2 or difference.count(-1) > 2:
        return False

    if not validate_wives(new_state):
        return False

    return True


def generate_random_state(old_state) -> list:
    number_of_couples = int((len(old_state) - 1) / 2)
    new_state = []

    # untill we have a valid new state
    while not validate_new_state(old_state, new_state):
        new_state = []
        for i in range(0, number_of_couples * 2 + 1):
            new_state.append(random.choice([1, 2]))

    return new_state


def hillclimbing_strategy(number_of_couples: int):
    state = get_initial_state(number_of_couples)

    if is_final_state(state):
        print("Final State!")
        return True

    best = 0
    local = False

    while not local:
        new_state = generate_random_state(state)
        # print(f"[80]: {new_state}")
        score = heuristic_function(new_state)
        # print(score)
        while True:
            candidate_state = generate_random_state(state)
            # print(heuristic_function(candidate_state))
            if heuristic_function(candidate_state) >= score:
                new_state = candidate_state
                print(f"[87]: {new_state}")
                break
            else:
                local = True

        if heuristic_function(new_state) > best:
            best = heuristic_function(new_state)
            state = new_state
