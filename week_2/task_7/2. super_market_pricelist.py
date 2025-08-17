items = ["apple", "banana", "cherry", "Eggs", "Cheese"]

# users input the price for the items
item1_price = int(input("input price from item 1:  "))
item2_price = int(input("input price from item2:  "))
item3_price = int(input("input price from item 3:  "))
item4_price = int(input("input price from item4:  "))
item5_price = int(input("input price from item 5:  "))
# add price to each items
stock_items = {
  items[0]:item1_price,
  items[1]:item2_price,  items[2]:item3_price,
  items[3]:item4_price,
  items[4]:item5_price}

print(stock_items)
# print available items
print(stock_items.keys())
print(stock_items.values())
stock_items.update({items[2]:"maize"})
# print updated list
print(stock_items)

