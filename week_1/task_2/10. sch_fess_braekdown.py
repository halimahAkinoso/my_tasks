# School fees Break down
# ask for school name
sch_name = input("Enter School name: ")
# ask for school tuition fee
tuition_fee = float(input("Enter Tuition fee: "))
# ask for school hostel fee
hostel_fee = float(input("Enter hostel fee: "))
# ask for school feeding fee
feeding_fee = float(input("Enter Feeding fee: "))

total= tuition_fee+hostel_fee+feeding_fee
print(f"The following is the breakdown of your ward school bill: \n Tuition fee is ₦{tuition_fee:,.2f}\n Hostel fee is: ₦{hostel_fee:,.2f} \n Feeding_fee is: ₦{feeding_fee:,.2f} \n The total of your bill is ₦{total:,.2f}")