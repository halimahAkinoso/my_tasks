#5 Ask a user to enter three items for their shopping list

item1 = input("Enter your first item: ")
item2 = input("Enter your second item: ")
item3 = input("Enter your third item: ")

shopping_list = (item1, item2, item3)
items_list= list(shopping_list)

# then ask for two more items to add.
items_list.append(input(("Enter your fourt item: ")))
items_list.append(input(("Enter your fifth item: "))
)
# List back to Tuple
shopping_list = tuple(items_list)
print(shopping_list)
print(" | ".join(shopping_list))
# print(items_list)
