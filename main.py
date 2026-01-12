
from analyzer import analyze_numbers, print_report
from storage import save_numbers, load_numbers, save_report 

def collect_numbers():
    numbers = []
    
    while True:
        try:
            num_count = int(input("How many numbers do you want to enter? "))
            if num_count < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for i in range(num_count):
        while True:
            try:
                number = float(input(f"Enter number {i+1}: "))
                numbers.append(number)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    return numbers

def main():
    numbers = []
    last_results = None

    while True:
        # show menu options
        print("\nMenu:")
        print("1) Enter numbers")
        print("2) Save numbers to JSON")
        print("3) Load numbers from JSON")
        print("4) Analyze current numbers")
        print("5) Save analysis report to file")
        print("6) Exit the program")

        choice = input("Choose an option(1-6): ").strip()

        if choice == '1':
            numbers = collect_numbers()
            print("Numbers saved in memory.")

        elif choice == '2':
           if not numbers:
              print("No numbers in memory to save. Please enter numbers first.")
           else:
              save_numbers(numbers)
              print("Numbers saved to data.json")

        elif choice == '3':
            numbers = load_numbers()
            if not numbers:
                print("No numbers found in data.json.")
            else:
                print("Numbers loaded from data.json:", numbers)

        elif choice == '4':
            if not numbers:
                print("No numbers in memory to analyze. Please enter or load numbers first.")
            else:
                last_results = analyze_numbers(numbers)
                print_report(last_results)

        elif choice == '5':
           if last_results is None:
              print("No analysis results to save. Run option 4 first.")
           else:
              save_report(last_results)
              print("Analysis report saved to report.txt")
              
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

         
      
if __name__ == "__main__":
    main()