# """"
# while loop = execute code while some condition remains true

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name ")
    name = input("Enter your name: ")
print(f"Hello {name}")

# For Loops = execute a block of code a fixed number of times.
# You can iterate over a range ,string ,sequence , etc.


for x in range(1, 11, 2):
    print(x)

print("Happy new year")

credit_number = "1234-6578-9012-3456"

# Nested Loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    print(x)

# """

# Collection = single "variable" used to store multiple values
# List = [] orderd and changeable. Duplicates are OK
# Set = {} unorderd and immutable, but Add/Remove OK. NO duplicates
# Tuple = () orderd and unchangeable. Duplicates OK. FASTER

# Lists
fruits = ["orange", "coconut", "apple", "banana"]

print(dir(fruits))  # all the methods and attributes that can be used with lists [].

for fruit in fruits:
    print(fruit)

# sets
cars = {"BMW", "Mazda", "Toyota", "Landrover"}

print(dir(cars))  # methods supported by sets
print(len(cars))

# Tuple
attitude = ("arrogant", "abusive", "kind", "Obedient")

print(dir(attitude))  # methods supported by tuples
print(len(attitude))
# they are immutable and accepts duplicates
