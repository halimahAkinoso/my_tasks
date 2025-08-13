# shopping empty list
empty_list = []
item1 = input("Enter your first shopping item: ")
item2 = input("Enter your second shopping item: ")
item3 = input("Enter your third shopping item: ")
# empty_list = item1 + ',', item2  +',',  item3
# print(empty_list)
empty_list.append(item1)
empty_list.append(item2)
empty_list.append(item3)
print(",".join(empty_list))
