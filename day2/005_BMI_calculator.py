# QUE: write a program that calculate the body mass index, BMI from a user weight and height.
# warnig: you should round the result to the nearest whole number.

height = input("Enter your height in m: ")
weight = input("Enter you weight in kg: ")

bmi = round(float(weight) / float(height)**2) # Round the result to the nearest whole number  
bmi2 = int(float(weight) / float(height)**2) # Convert the result to integer which will remove the decimal point

print("bmi: ", bmi)
print("bmi2: ", bmi2)