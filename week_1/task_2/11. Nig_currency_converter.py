# Nigeria currency converter
# Ask user amount in naira
naira_amount = float(input("Enter amount in Naira: "))
dollar =float(input("Enter exchange rate in US Dollars: "))
pounds = float(input("Enter Exchange rate for British Pounds: "))
dollar_conversion = naira_amount * dollar

pounds_conversion = naira_amount * pounds

# print(f"Nigerian Currency Converter for different country is as follows: \n Exchange Rate to US Dollars ${dollar_conversion:,.2f} \n Exchange rate to British Pounds is £{pounds_conversion:,.2f}")

print("\nNigerian Currency Converter")
print("-" * 40)
print(f"{'Currency':<20}{'Amount':>18}")
print("-" * 40)
print(f"{'US Dollars ($)':<20}${dollar_conversion:>17,.2f}")
print(f"{'British Pounds (£)':<20}£{pounds_conversion:>17,.2f}")
print("-" * 40)