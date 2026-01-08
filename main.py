def analyze_numbers(numbers):
    # Return count, min, max, sum, average in a dictionary
    if not numbers:
        return {
            "count": 0,
            "min": None,
            "max": None,
            "sum": 0,
            "average": None
        }
    
    return {
        "count": len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers)
    }


def main():
    while True:
        # show menu options
        print("\nMenu:")
        print("1) Enter numbers and analyze")
        print("2) Exit the program")
        choice = input("Choose an option(1 or 2): ").strip()
        if choice == '2':
            print("Exiting the program. Goodbye!")
            break
        elif choice != '1':
            print("Invalid choice. Please select 1 or 2.")
            continue
         # Ask the user how many numbers to enter
        while True:
          try:
            num_count = int(input("How many numbers would you like to enter? "))
            if num_count < 0:
                print("Please enter a non-negative number.")
                continue
            break
          except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    numbers = []
    
    # Loop to collect inputs
    for i in range(num_count):
        while True:
            try:
                # Validate each input is a number
                number = float(input(f"Enter number {i + 1}: "))
                # Store numbers in a list
                numbers.append(number)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    # Print the list
    print("\nYour numbers:", numbers)


    # Analyze the numbers
    results = analyze_numbers(numbers)
    print("\nAnalysis Results:")
    print(f"Count: {results['count']}")
    print(f"Min: {results['min']}")
    print(f"Max: {results['max']}")
    print(f"Sum: {results['sum']}")
    print(f"Average: {results['average']}")
        
      
if __name__ == "__main__":
    main()