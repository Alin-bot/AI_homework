import sys 
import os
sys.path.append(os.path.abspath("~/.."))
from backtracking_strategy import *
from jealous_husbands import get_initial_state

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