from jealous_husbands import is_final_state, get_initial_state
import random


def heuristic_function(state: list) -> int:
    nr = 0
    for i in range(1, len(state)):
        if state[i] == 2:
            nr += 1
    return nr


def check_wife_without_husband_and_not_single(state, wife_index):
    if state[wife_index] == state[wife_index - 1]:
        return False
    else:
        for i in range(2, len(state), 2):
            if state[wife_index] == state[i]:
                return True
    return False


def validate_state(state):
    if state == []:
        return False

    for i in range(1, len(state), 2):
        if check_wife_without_husband_and_not_single(state, i):
            return False
    return True


def validate_new_state(old_state, new_state):
    if new_state == []:
        return False

    difference = []
    for list1_i, list2_i in zip(old_state, new_state):
        difference.append(list1_i - list2_i)

    # The boat didn't move
    if difference[0] == 0:
        print("barca")
        return False

    for i in range(1, len(difference)):
        if difference[i] != 0 and old_state[i] != old_state[0]:
            print("1")
            return False

    if len(difference) - difference.count(0) - 1 > 2:
        print("2")
        return False

    if difference.count(0) == len(difference):
        print("3")
        return False

    count = 0
    if difference[0] != 0:
        for i in range(1, len(difference)):
            if difference[i] == 0:
                count += 1
        if count == len(difference) - 1:
            print("4")
            return False

    return True


def generate_random_state(n: int, old_state):
    state = []
    while not validate_new_state(old_state, state):
        state = []
        for i in range(1, n * 2 + 2):
            state.append(random.choice([1, 2]))
    print(old_state)
    return state


def hillclimbing_strategy(state):
    if is_final_state(state):
        print("Final State!")
        return True

    best = 0
    local = False
    score = 0

    while not local:
        new_state = generate_random_state(int((len(state) - 1) / 2), state)
        print(f"[75]: {new_state}")
        score = heuristic_function(new_state)
        while True:
            candidate_state = generate_random_state(int((len(state) - 1) / 2), state)
            if heuristic_function(candidate_state) > score:
                new_state = candidate_state
                print(f"[82]: {new_state}")
                break
            else:
                local = True
        if heuristic_function(new_state) > best:
            best = heuristic_function(new_state)
            state = new_state


# t := 0
# initialize best
# repeat
#     local := FALSE
#     select a candidate solution (bitstring) vc at random
#     evaluate vc
#     repeat
#         vn := Improve(Neghborhood(vc))
#  	if eval(vn) is better than eval(vc)
# 	then vc := vn
# 	else local := TRUE
#     until local
#     t := t + 1
#     if vc is better than best
#     then best := vc
# until t = MAX

# print(generate_random_state(3))
# print(validate_state([]))
# print(validate_state(get_initial_state(3))) # -> TRUE
# print(validate_state([1, 2, 1, 2, 2])) # -> FALSE


# print(validate_new_state(get_initial_state(2), [1, 1, 2, 2, 1])) # -> barca nu s a mutat (False)
# print(validate_new_state([1, 2, 1, 1, 1], [2, 1, 2, 1, 1])) # -> mutare simetrica a 2 persoane (False)
# print(validate_new_state(get_initial_state(2), [2, 2, 2, 2, 2])) # -> too many moves (False)
# print(validate_new_state(get_initial_state(2), [2, 2, 2, 1, 1])) # -> True
# print(validate_new_state(get_initial_state(3), [1, 1, 2, 2, 2, 2, 1])) # -> False
# print(validate_new_state(get_initial_state(2), [2, 1, 1, 1, 1])) # -> False

# hillclimbing_strategy(get_initial_state(3))

# print(generate_random_state(3, get_initial_state(3)))
