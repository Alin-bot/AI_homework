from jealous_husbands import is_final_state, get_initial_state
from queue import PriorityQueue

def heuristic_function(state: list) -> int:
    nr = 0
    for i in range(1, len(state)):
        if state[i] == 2:
            nr += 1
    return nr

def get_sorted_queue_of_neighbours_of_state(state: list):
    # final score needs to be score + 1
    return list

def a_star_strategy(number_of_couples: int):
    state = get_initial_state
    best_score = number_of_couples * 2
    sorted_queue = get_sorted_queue_of_neighbours_of_state(state)

    while sorted_queue.first().score() < best_score:

        if is_final_state(sorted_queue.first()):
            best_score = sorted_queue.first().score()

        sorted_queue.first().explored = True

        sorted_queue.add(get_sorted_queue_of_neighbours_of_state(sorted_queue.first()))

        if duplicates_states in sorted_queue:
            sorted_queue.keep(lowest_score)

        sorted_queue.sort()



