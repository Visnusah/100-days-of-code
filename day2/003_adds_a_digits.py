# Q: WAP that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

number_from_user = int(input("Enter a two digit number: \n"))
number_char = str(number_from_user)
print("The sum of the digits in the number is : " + number_char[0] + " + " + number_char[1] + " = " + str(int(number_char[0]) + int(number_char[1])))