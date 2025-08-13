# Electricity Bill Formatter
# ask the user for customer name
name = input("Enter customer full name: ")
unit_consume = int(input("Enter unit consume per KWh"))
cost = float(input("Enter cost per unit: "))     
total_bill = unit_consume * cost
# print("The total bill for " ,name ,"\n is", total_bill)           
print(f"Total bill for {name} is ₦{total_bill:,.2f}")