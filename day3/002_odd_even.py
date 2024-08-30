# QUE: WAP to check if the given number is odd or even.

print("Welcome to the odd-even checker!")
number = int(input("Enter a number: "))

if number % 2 == 0:
  print(f"{number} is an even number.")
else:
  print(f"{number} is an odd number.")