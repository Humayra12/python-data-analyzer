def main():
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

if __name__ == "__main__":
    main()