
# ask users to input their name
mem_1 = input("Please enter your name: ").split(",")
mem_2 = input("Please enter your name: ").split(",")
mem_3 = input("Please enter your name: ").split(",")

# add user input
members_name= mem_1 + mem_2 + mem_3
# convert to set
set_of_members = set(members_name)
print(set_of_members)
#print length of the values
set_of_members = {name: len(name) for name in set_of_members}
print(set_of_members)
# {name: len(name) for name in set_of_names}