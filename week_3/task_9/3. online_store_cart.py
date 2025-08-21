item = ["Rice", "Beans", "Custard", "Macaroni"]
prices =[2500, 1350, 1750, 1150]

cart_total = 0

for price in prices:
  cart_total += int(price)
  print(cart_total)
  print(f"Items: {item}\nTotal: {cart_total}")