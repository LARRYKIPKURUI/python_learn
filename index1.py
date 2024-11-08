# """
# input() = Its a function that prompts the user to enter
# data and returns the  data as a string

name = input("What is your name?: ")
age = input("What is your age?: ")

print(f"Your name is {name} and you are {age} years old!")

import math

x = 3.14
result = round(x)

print(result)

print(math.pi)

# Conditions
# ANY CODE WRITTEN UNDER IF IS INDENTED!!

age = int(input("Enter your age: 1"))

if age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You havent been born yet")
else:
    print("You must be 18+ to sign up")

# String Methods

name = input("Enter your full name: ")

result = len(name)  # indicates how many characters are in the var
print(result)
# """

# validate user input exercise
# 1. Username is no more than 12 characters
# 2. Username must not contain spaces
# 3. Username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username cant be more than 12 characters")
elif not username.find(" ") == -1:
    print("Username cannot contain spaces")
elif not username.isalpha():
    print("Username cannot contain numbers")
