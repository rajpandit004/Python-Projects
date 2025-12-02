print("=============================")
print("WELCOME TO THE TIP CALCULATOR")
print("=============================")

total_bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
no_of_people = int(input("How many people to split the bill?\n"))

# Calculate the bill with tip
bill_with_tip = total_bill + (total_bill * tip / 100)

# Split the bill equally among specified no of people and print it
print(f"Each person should pay: ${round(bill_with_tip / no_of_people, 2)}")
