#QUE: WAP to check whether the given year is leap year or not.
# example input: 2000
# 2000 / 4 = 500 (leap year)
# 2000 / 100 = 20 (not leap year)
# 2000 / 400 = 5 (leap year)
# example output: Leap year 

# on every leap year that is divisible by 4,
 # except every year that is evenly divisible by 100,
  # unless the year is also evenly divisible by 400.
  
year = int(input("Enter the year: "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not a leap year")
  else:
    print("Leap year")
else:
  print("Not a leap year")