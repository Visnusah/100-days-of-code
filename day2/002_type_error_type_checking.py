num_char = len(input("What is your name?\n"))
# print("Your name has " + num_char + " characters.")
# Output: TypeError: can only concatenate str (not "int") to str

# TO fix the above error, we need to convert the integer to string

print("Your name has " + str(num_char) + " chraacters.") 