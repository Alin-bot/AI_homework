import sys 
import os
sys.path.append(os.path.abspath("~/.."))
from hillclimbing_strategy import *
from jealous_husbands import get_initial_state

# print(validate_state([]))
# print(validate_state(get_initial_state(3))) # -> TRUE
# print(validate_state([1, 2, 1, 2, 2])) # -> FALSE


# print(validate_new_state(get_initial_state(2), [1, 1, 2, 2, 1])) # -> barca nu s a mutat (False)
# print(validate_new_state([1, 2, 1, 1, 1], [2, 1, 2, 1, 1])) # -> mutare simetrica a 2 persoane (False)
# print(validate_new_state(get_initial_state(2), [2, 2, 2, 2, 2])) # -> too many moves (False)
# print(validate_new_state(get_initial_state(2), [2, 2, 2, 1, 1])) # -> True
# print(validate_new_state(get_initial_state(3), [1, 1, 2, 2, 2, 2, 1])) # -> False
# print(validate_new_state(get_initial_state(2), [2, 1, 1, 1, 1])) # -> False
# print(validate_new_state(get_initial_state(2), [1, 1, 1, 1, 1])) # -> False


hillclimbing_strategy(3)

# print(generate_random_state(get_initial_state(3)))
