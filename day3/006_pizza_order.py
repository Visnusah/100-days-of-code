# QUE: WAP to take pizza order from user and calculate the total cost of pizza.

print("welome to python pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_chese = input("Do you want extra chese? Y or N: ")

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
      bill += 2
    if extra_chese == "Y":
      bill += 1
    print(f"Your final bill is: ${bill}")
elif size == "M":
  bill = 20
  if add_pepperoni == "Y":
    bill += 3
    if extra_chese == "Y":
      bill += 1
    print(f"your final bill is: ${bill}")
elif size == "L":
  bill = 25
  if add_pepperoni == "Y":
    bill += 3
    if extra_chese == "Y":
      bill += 1
    print(f"Your final bill is: ${bill}")
else:
  print("Invalid input")