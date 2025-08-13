# Daily market report
# ask user to input market name
market_name = input("Enter market name: ")
traders_num = input("Enter number of traders: ")
daily_rev = float(input("Enter daily revenue in naira: "))
# print("This is the market report for ", market_name, "with the total numbers of ",traders_num, "traders", "with the total revenue of ", daily_rev)
print(f"This is the market report for {market_name} with the total number of {traders_num} traders, with the total revenue of ₦{daily_rev:,.2f}")