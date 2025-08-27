item = ["Rice", "Beans", "Custard", "Macaroni"]
prices =[2500, 1350, 1750, 1150]

cart_total = 0

for price in prices:
  try:
    cart_total += int(price)
  except ValueError:
    print(f"caution:cannot convert {price} to an integer")
  except Exception as e:
    print(f"An unexpected error occurred: {e}. Skip this item")
  print(cart_total)
  print(f"Items: {item}\nTotal: {cart_total}")