# Simulated USSD Menu Interaction for mobile service

# 1. Welcome Message
print("Welcome to Nageria USSD Banking!\nN6.98 will be debited from your airtime balance for banking services on this channel.")

# 2. Ask user to dial a USSD code
ussd_code = input("Dial a USSD code (e.g., *123#): ")

# 3. Print menu with newline escape sequences
menu = "1. Check Balance\n2. Buy Airtime\n3. Buy Data"
print("\nPlease select a service:\n" + menu)

# 4. Ask user to choose an option
option = input("Enter your choice (1, 2, or 3): ")

# 5. Display confirmation message
if option == "1":
    print(f"\nYou selected: Check Balance")
    print("Your account balance is ₦5,000.00")
elif option == "2":
    print(f"\nYou selected: Buy Airtime")
    amount = float(input("Enter amount of airtime to buy: ₦"))
    print(f"You have successfully purchased ₦{amount:,.2f} airtime.")
elif option == "3":
    print(f"\nYou selected: Buy Data")
    amount = float(input("Enter amount of data to buy (in MB): "))
    print(f"You have successfully purchased {amount:,.0f}MB data.")
else:
    print("\nInvalid option selected.")

# 7. Final summary message
print("\nThank you for using Nigeria USSD")