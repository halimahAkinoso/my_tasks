# Transport fare calculator
# ask for distance in kilometer
distance = float(input("Enter the distance: "))
# ask for fare per km
fare = float(input("Enter fare per km: "))
total_fare = distance* fare
print(f"Total fare is ₦{total_fare:.2f}")