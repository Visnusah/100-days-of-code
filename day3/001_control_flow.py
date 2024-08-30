# QUE: WAP to check if the user is eligible to ride the rollercoaster based on their height.

print("Wlcome to the rollercoaster!")
age = int(input("enter your age: "))
height = int(input("Enter your hieght in cm: "))

if height > 120:
  print("You can ride the rollercoaster!")
  if age <= 12:
    print("please pay bill of $5.")
  elif age <= 18:
    print("please pay bill of $7.")
  else:
    print("please pay bill of $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")