# Number manupalation in python

a = 8/3
b = 8//3
c = int(a)
d = round(a)

print(a) # 2.6666666666666665
print(c) # 2
print(d) # 3
print(b) # 2

print(type(a)) # float
print(type(b)) # int
print(type(c)) # int
print(type(d)) # int


# f-string
score = 0
height = 1.8
iswinning = True

print("your score is "+ str(score) +", "+ "height is "+str(height)+" and you are winning: "+str(iswinning) )

print(f"your score is {score}, height is {height} and you are winning: {iswinning}")