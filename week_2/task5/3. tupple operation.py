# tupple operations
# create a tupple of five Nigerian state enter by user
state1 = input("Enter any nigeria state 1: ")
state2 = input("Enter any nigeria state 2: ")
state3 = input("Enter any nigeria state 3: ")
state4 = input("Enter any nigeria state 4: ")
state5 = input("Enter any nigeria state 5: ")
state = (state1, state2, state3, state4, state5)
print(state)
# print first and last state
print(state[0],state[4])
if ("Lagos" in state):
    print("yes")
print(len(state))