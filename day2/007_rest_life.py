# QUE: create program using maths and f-string that tells us how many days weeks months we have left if we live until 90 years old.
# Don't edit the code below ⬇️
age = input("What is your current age? ")

# Code from here ➷
age_in_int = int(age)  # Convert the input age from string to integer

years_left = 90 - age_in_int  # Calculate the years left until 90
weeks_left = years_left * 52  # Convert years left to weeks
months_left = years_left * 12  # Convert years left to months
days_left = years_left * 365  # Convert years left to days

# Output the days, weeks, and months left using formatted string
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")