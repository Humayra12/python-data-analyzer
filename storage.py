# storage.py
# Create a function save_numbers(numbers,
# It should save the list of numbers to a JSON file as a
# Use indent=2 for readable formatting
# Overwrite the file if it exists
# Do not print anything in this function

import json

def save_numbers(numbers, filename="data.json"):
    data = {"numbers": numbers}
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)

