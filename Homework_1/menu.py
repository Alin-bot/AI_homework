from backtracking_strategy import bkt_strategy
from hillclimbing_strategy import hillclimbing_strategy
from astar_strategy import a_star_strategy
from bfs_strategy import bfs_strategy

strategies = {
    "1": {"function": bkt_strategy},
    "2": {"function": bfs_strategy},
    "3": {"function": hillclimbing_strategy},
    "4": {"function": a_star_strategy},
}
stop = False
while not stop:
    change_couples = False
    while not change_couples:
        number_of_couples = input("Please enter the number of couples:")
        change_strategy = False
        while not change_strategy:
            print("Please choose a strategy from the following:")
            print("[1] Backtracking")
            print("[2] BFS")
            print("[3] Hillclimbing")
            print("[4] A-star")
            strategy_index = input()
            strategies[strategy_index]["function"]()
            print("Change strategy? Type Y/N")
            if input() == "Y":
                change_couples = False
            else:
                print("Change number of couples? Type Y/N")
                if input() == "Y":
                    change_couples = True
                    change_strategy = True
