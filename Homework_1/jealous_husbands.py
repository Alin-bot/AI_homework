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
