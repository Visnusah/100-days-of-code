#QUE: WAP to calculate the BMI of a person and print the result.

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / height **2)
if bmi < 18.5:
  print(f"You BMI is {bmi} and you are uderweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi} and you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi} and you are overweight.")
else:
  print(f"Your BMI is {bmi} and you are obese.")