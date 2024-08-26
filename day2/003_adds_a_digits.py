# Q: WAP that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

number_from_user = int(input("Enter a two digit number: \n"))

# first way
number_char = str(number_from_user)
print("The sum of the digits in the number is : " + number_char[0] + " + " + number_char[1] + " = " + str(int(number_char[0]) + int(number_char[1])))

# second way
digits = str(number_from_user)
first_digit = int(digits[0])
second_digit = int(digits[1])

result = first_digit + second_digit
print("The sum of the digits in the number is : " + str(first_digit) + " + " + str(second_digit) + " = " + str(result))