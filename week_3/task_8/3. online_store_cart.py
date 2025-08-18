items =["book", "cardnoard", "gum", "erazer"]
prices = ["400", "200", "1500", "100"]

cart_total = 0

# add price of some items into cart_total
for price in prices:
    cart_total += price
print(cart_total)
print(f"Items: {items}\nTotal Price: {cart_total}")