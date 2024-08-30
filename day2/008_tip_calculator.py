# QUE: If the bill was $150.00, split between 5 people, with 12% tip. Each person should pay (150.00 / 5) * 1.12 = 33.6
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal places.

print("Welcome to the tip calculator!")  # Greeting message for the user
bill = float(input("What was the total bill? $"))  # Input for total bill amount
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))  # Input for tip percentage
people = int(input("How many people to split the bill? "))  # Input for number of people sharing the bill
bill_as_percentage =  tip / 100  # Convert tip percentage into a decimal
total_tip_amount = bill * bill_as_percentage  # Calculate the total tip amount
total_bill = bill + total_tip_amount  # Calculate the total bill including tip
bill_per_person = round((total_bill / people), 2)  # Calculate and round the bill per person
bill_per_person = "{:.2f}".format(bill_per_person)  # Format the bill per person to 2 decimal places
print(f"Each person should pay: ${bill_per_person}")  # Output the amount each person should pay