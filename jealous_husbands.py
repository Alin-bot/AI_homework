from inspect import signature

def get_initial_state(number_of_couples:int):
    initial_state = [1] * (1 + number_of_couples * 2)
    return initial_state

def is_final_state(state:list)->bool:
    return all(element == 2 for element in state) and (len(state) % 2 == 1)

def transition(state:list, male_1:int=-1, female_1:int=-1, male_2:int=-1, female_2:int=-1)->list:
    if not validate_transition(state, male_1, female_1, male_2, female_2):
        raise Exception("Transition not allowed!")

    if state[0] == 1:
        state[0] = 2
    else:
        state[0] = 1

    for person in [male_1, female_1, male_2, female_2]:
        if person != -1:
            if person == male_1 or person == male_2:
                state[2*person] = state[0]
            elif person == female_1 or person == female_2:
                state[2*person-1] = state[0]
    
    return state

def validate_transition(state:list, male_1:int=-1, female_1:int=-1, male_2:int=-1, female_2:int=-1)->bool:

    if state[0] == 1:
        state[0] = 2
    else:
        state[0] = 1
    
    ok = 0
    for person in [male_1, male_2, female_1, female_2]:
        if person != -1 and (person in [female_1, female_2]):
            if state[person*2] == state[0]:
                ok = 1
            for male in range(2, len(state), 2):
                if state[male] == state[0] and ok == 0:
                    return False
        elif person != -1 and (person in [male_1, male_2]):
            state[person*2] = state[0]

    return True

# print(get_initial_state(5))             #should print inistial state list

# print(is_final_state([2, 1, 2, 2, 2]))  #should print False
# print(is_final_state([2, 2, 2, 2]))     #should print False
# print(is_final_state([2, 2, 2, 2, 2]))  #should print True

# print(transition(get_initial_state(5), male_1 = 1, female_1 = 3))

# print(validate_transition(get_initial_state(5), male_1 = 1, female_1 = 1))  # true
# print(validate_transition([1,1,2,1,1], male_1 = 2, female_1 = 1))           # husband is on the future side and the female wants to get on the side with another male (true) 
# print(validate_transition([1,1,1,1,1], male_1 = 2, female_1 = 1))           # female wants to get on the other side with another male and her husbant stays on the initial side (false)
# print(validate_transition([1,1,1,1,2], female_1 = 1))                       # female wants to get on the side where there is another male (false)

# print(transition(get_initial_state(5), male_1 = 1, female_1 = 1))
# print(transition([1,1,2,1,1], male_1 = 2, female_1 = 1))
# print(transition([1,1,1,1,1], male_1 = 2, female_1 = 1)) 
# print(transition([1,1,1,1,2], female_1 = 1))
