print("Wlcome to the rollercoaster!")
age = int(input("enter your age: "))
height = int(input("Enter your hieght in cm: "))

if height > 120:
  print("You can ride the rollercoaster!")
  if age <= 12:
    bill = 5
    print("child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("youth tickets are $7.")
  else:
    bill = 12
    print("adult tickets are $12.")
  wants_photo = input("Do you want a photo taken? Y or N: ")
  if wants_photo == "Y" or wants_photo == "y": # or is used to check multiple conditions
    bill += 3
    print(f"your total bill is ${bill}")
else:
  print("Sorry, you have to grow taller before you can ride.")