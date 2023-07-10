print("Welcome to the tip calculator.")
total_bill=float(input("What was the total bill? $"))
percentage=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split=int(input("How many people to split the bill? "))
bill=(percentage/100)*total_bill
final_amount=round((bill+total_bill)/split,2)
sum="{:.2f}".format(final_amount)
print(f"Each person should pay: ${sum}")


# Output
# Welcome to the tip calculator.
# What was the total bill? $150
# What percentage tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 5
# Each person should pay: $33.60