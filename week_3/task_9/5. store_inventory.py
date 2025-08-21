# Create a dictionary called store
store = {"Book": 10, "Pen": 20, "Bag": 5}  


# print initail state of dictionary 
print(f"Stock in store before purchase: {store}")
# ask user to enter the item they want to buy
item_purchase = input ("Enter the item you want to buy: ")

# ask user to enter the quantity of item they want to buy

item_quantity = int(input("Enter the quantity you want to purchase: "))

# Available items in the store
before_purchase = {item: quantity for item, quantity in store.items()}
# ASSIGNMENT Operator to update the item quantity in the store
if item_purchase in store and store[item_purchase] >= item_quantity:

    # If the item is in the store and the quantity is sufficient, update the store
    store[item_purchase] -= item_quantity
else:
    print("Insufficient quantity")
store[item_purchase] -= item_quantity 

print(f"Stock in store after purchase: {store}")