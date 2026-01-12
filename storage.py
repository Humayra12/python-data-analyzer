# storage.py
# Create a function save_numbers(numbers,
# It should save the list of numbers to a JSON file as a
# Use indent=2 for readable formatting
# Overwrite the file if it exists
# Do not print anything in this function

import json

from datetime import datetime

def save_numbers(numbers, filename="data.json"):
    data = {"numbers": numbers}
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)

def load_numbers(filename="data.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data.get("numbers", [])
    except FileNotFoundError:
        return [] #Return empty list if file does not exist 
    
def save_report(results, filename="report.txt"):
    with open(filename, "w") as file:
        file.write("Analysis Report\n")
        file.write(f"Generated on: {datetime.now()}\n\n")
        file.write(f"Count: {results['count']}\n")
        file.write(f"Min: {results['min']}\n")
        file.write(f"Max: {results['max']}\n")
        file.write(f"Sum: {results['sum']}\n")
        file.write(f"Average: {results['average']}\n")
