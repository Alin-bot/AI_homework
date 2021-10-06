def get_initial_state(number_of_couples:int):
    initial_state = [1] * (1 + number_of_couples * 2)
    return initial_state

def is_final_state(state:list)->bool:
    return all(element == 2 for element in state) and (len(state) % 2 == 1)


print(get_initial_state(5))             #should print inistial state list
print(is_final_state([2, 1, 2, 2, 2]))  #should print False
print(is_final_state([2, 2, 2, 2]))     #should print False
print(is_final_state([2, 2, 2, 2, 2]))  #should print True
