# """
# Iterables = An object/collection that can return its elemnts one at a time,
#               allowing it to be iterated over in a loop.

numbers = [1, 2, 3, 4, 5, 6]

for num in reversed(numbers):
    print(num)

    # Lists, Tuples ,Sets  and Dictionaries are considerd iterable.

# Membership operators = Used to test whether a value or variable is found in a
#           sequence (string,list,tuple,set, or dictionary)
#                       1. in
#                       2. not in

word = "APPLE"

letter = input("Guesss a letter in the secret word : ")

if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"There is a letter {letter}")

students = {"larry", "robert", "ndungu"}

student = input("Enter the name of the student: ")

if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} is a student")

grades = {
    "Sandy": "A",
    "Mandy": "B",
    "Grandy": "C",
}

student = input("Enter the name of the student: ")

if student in grades:
    print(f"{student}s grade is {grades[student]}")
else:
    print(f"{student} doesnt exist")

email = "larrykipkurui12@gmail.com"

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")

# List comprehension = A concise way to create lists in python
#                       compact and easier to read than traditional loops.
#    formula =   [expression for value in iterable if condition]


doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

print(doubles)
print(triples)
print(squares)

fruits = ["apple", "banana", "coconut", "kiwi", ]
fruits = [fruits.upper() for fruit in fruits]

print(fruits)

# module = a file containing code you want to include in your
#           program , use 'import' to include a module (built-in or your own).
#           useful to break up a large program by reusing separate files

# print(help("modules"))  #All modules supported by python


import math

print(math.pi)

import create_module

result = create_module.pi

print(result)


# Variable scope = where a variable is visible and accessible
# scope resulution = Oder = (LEGB) Local -> Enclosed -> Global -> Built-In

def func1():
    a = 1
    print(a)


# A variable declared in a function is only visible to itself and not in another function

def func2():
    print(x)


def func3():
    print(x)


x = 1
func2()
func3()
#   The output for both functions is 1 ..because x is now a global varibale
#   declared outside of both functions

from math import e

print(e)


def func4():
    print(e)


func4()


# The above is a Built in variable.


# if __name__ == __main__: (this script can be imported Or run standalone)
#                           Functions and classes in this module can be reused
#                            without the main block of code executing

def main():
    if __name__ == "__main__":
        main()

# """
