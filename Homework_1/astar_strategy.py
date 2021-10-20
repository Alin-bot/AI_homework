from jealous_husbands import is_final_state, get_initial_state, transition
from queue import PriorityQueue
from hillclimbing_strategy import validate_new_state, validate_wives
from operator import itemgetter


def heuristic_function(state: list) -> int:
    nr = 0
    for i in range(1, len(state)):
        if state[i] == 2:
            nr += 1
    return nr


def get_sorted_queue_of_neighbours_of_state(state: list):
    queue = []
    sorted_queue = []
    for index_1 in range(1, len(state)):
        for index_2 in range(1, len(state)):
            state_copy = state.copy()
            candidate_state = transition(state_copy, index_1, index_2)
            if validate_new_state(state, candidate_state):
                score = heuristic_function(candidate_state)
                queue.append(
                    {
                        "state": candidate_state,
                        "score": score + 1,  # final score needs to be score + 1
                        "status": "Unexplored",
                    }
                )
    sorted_queue = sort_queue_by_key(queue, "score")
    return sorted_queue


def sort_queue_by_key(queue: list, key_dict: str):
    sorted_queue = sorted(queue, key=itemgetter(key_dict))
    return sorted_queue


def remove_duplicates_from_queue(sorted_queue: list):
    for i in range(len(sorted_queue) - 2):
        for j in range(i + 1, len(sorted_queue) - 1):
            print(i, j)
            print(sorted_queue[i]["state"] == sorted_queue[j]["state"])
            if (
                sorted_queue[i]["state"] == sorted_queue[j]["state"]
                and sorted_queue[i]["score"] < sorted_queue[j]["score"]
            ):
                sorted_queue.remove(j)
    return sorted_queue


def a_star_strategy(number_of_couples: int):
    state = get_initial_state(number_of_couples)
    best_score = number_of_couples * 2
    sorted_queue = get_sorted_queue_of_neighbours_of_state(state)

    i = -1
    while sorted_queue[i]["score"] < best_score:
        if sorted_queue[i]["status"] == "Unexplored":

            if is_final_state(sorted_queue[i]["state"]):
                best_score = sorted_queue[i]["score"]

            sorted_queue[i]["status"] = "Explored"

            sorted_queue.append(
                get_sorted_queue_of_neighbours_of_state(sorted_queue[i]["state"])
            )
            print(sorted_queue)

            # sorted_queue = remove_duplicates_from_queue(sorted_queue)
            # new_queue = sort_queue_by_key(sorted_queue, "score")
            # sorted_queue = new_queue.copy()
            i = -1
        else:
            i = i - 1
        return sorted_queue


queue = [
    {"state": [1, 1, 1, 2, 1], "score": 5, "status": "Unexplored"},
    {"state": [1, 1, 1, 1, 2], "score": 1, "status": "Unexplored"},
]

# print(sort_queue_by_key(queue, "score"))
# print(get_sorted_queue_of_neighbours_of_state([1, 1, 1, 1, 1]))
# print(a_star_strategy(2))
