# """
# 2d Collections/Dimensions

fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "sukuma", "cabbage"]
meats = ["chicken", "fish", "turkey", "goat"]

groceries = [fruits, vegetables, meats]

print(groceries[0])

for grocery in groceries:
    for food in grocery:
        print(food, end=" ")

# 2d tuple Numpad

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print

# Dictionary = A collection of {key:value} pairs orderd
#                and changeable. No duplicates

capitals = {
    "USA": "Washington",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesnt exist")

capitals.update({"Germany": "Berlin"})

keys = capitals.keys()
for key in capitals.key():
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)


# Functions
# Function = A block of reusable code place () after the function name to invoke it.

def happy_birthday(name, age):
    print(f"hAPPY bIRTHDAY {name}")
    print(f"hAPPY bIRTHDAY you are {age} yrs old")
    print(f"hAPPY bIRTHDAY")


happy_birthday("larry", 20)
happy_birthday("bernice", 3)
happy_birthday("chloe", 3)


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of {amount} is due {due_date} ")


display_invoice("Larry", 50000, "18/5/2025")


# return = statement used to end a function and send a result back to the caller.

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("larry", "kipkurui")

print(full_name)


# """
# Default arguments =  A default value for parameters, default is used
#                       when that argument is omitted to make your functions
#                      more flexible, reduces no of arguments
#                   1. positional, 2. DEFAULT, 3. Keyword , 4. arbitrary


def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)


print(net_price(500))

# On the above block of code discount and tax have a default value
# hence they are called default arguments

print(net_price(500, 0.1, 0))  # this will overide the default argument making the  arguments flexible

import time


def count(start, end):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("DONE!!")


count(6, 7)


# Keyword arguments = an argument preceded by an identifier
#                 helps with readability,
#                 order of arguments doesnt matter
#                1.positional, 2. default, 3. KEYWORD, 4. arbitary
def hello(greeting, title, first, last):
    print(f"{greeting},{title},{first},{last}")


hello("Hello", title="Mr.", last="Kipkurui", first="Larry")


# In the above code on line 124  we have  added keyword arguments so it will help us in that
# order won't matter as long AS POSITIONAL ARGUMENTS ARE FIRST HENCE HELLO IS PLACED FIRST
# AND NOWHERE ELSE.

# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#                *unpacking operator
#               1. positional 2. default 3. keyword 4. ARBITARY 


# arbitary = varying amount of arguments

# args = arguments
# kwargs = key word arguments

def add(*args):  # it collects args as a tuple
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1, 2, 3))


def display_name(*args):
    for arg in args:
        print(arg, end="")


display_name("Dr", "Larry", "Kipkurui", "Mkurugenzi")


# Kwargs

def print_address(**kwargs):  # It collects kwargs as a dictionary
    for key, value in kwargs.items():
        print(f"{key}:{value}")


print_address(street="olpul", city="Nairobi", state="Rongai", zip="2788")


# exercise
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()


shipping_label(
    "Dr", "Larry", "Kipkurui", "Mkurugenzi",
    street="olpul",
    city="Nairobi",
    state="Rongai",
    zip="2788"
)

shipping_label()
