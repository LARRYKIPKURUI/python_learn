# Python file detection
# """
import os

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"File {file_path} exists")

    if os.path.isfile(file_path):
        print(f"File {file_path} is a file")
    elif os.path.isdir(file_path):
        print(f"File {file_path} is a directory")
else:
    print("File does not exist")

# Python writing files (.txt, .json, .csv)

import json
import csv

employees = [
    ["Name", "Age", "Job"],
    ["spongebob", 30, "cook"],
    ["Patrick", 37, "Unemployed"],
    ["Sandy", 27, "Scientist"]
]

file_path = "C:/Users/larry/Desktop/output.csv"

try:
    with open(file=file_path, mode="w") as file:  # mode-w is for write and r is for read
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)

        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print(f"txt File  already exists")

# Python reading files (.txt, .json, .csv)
import csv

file_path = "C:/Users/larry/Desktop/output.csv"
try:
    with open(file=file_path, mode="r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("File does not exist")
except PermissionError:
    print("Permission denied")

import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%I:%M:%S %p")

target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()
if target_datetime < current_datetime:
    print(f"Target datetime has passed")
else:
    print(f"Target datetime has not passed")

# Multithreading = Used to perform multiple tasks concurrently (multitasking)
# Good for I/O tasks like files or fetching data from APIs
# threading. Thread  (target=my_function)

import threading
import time


def walk_dog():
    time.sleep(8)
    print("Walk the dog.")


def takeout_trash():
    time.sleep(2)
    print("Takeout the trash")


def get_mail():
    time.sleep(4)
    print("Get  the mail")


chore1 = threading.Thread(target=walk_dog)
chore1.start()

chore2 = threading.Thread(target=takeout_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are completed")

# """
#  Connecting to an api using Python

import requests

base_url = "https://pokeapi.co/api/v2/"


def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print("Something went wrong")


pokemon_name = "typhlosion"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"]} ")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]} ")
    print(f"Weight: {pokemon_info["weight"]} ")
