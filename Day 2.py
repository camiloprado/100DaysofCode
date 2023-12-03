print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
value = (total*((percent/100)+1))/people
print(f"Each person shouldpay: ${value:.2f}")