# robust_division_calculator.py

def display_menu():
    print("Menu:")
    print("1. Add to shopping list")
    print("2. View shopping list")
    print("3. Exit")

def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform division
        result = numerator / denominator
        return f"The result of the division is {result:.2f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."

if __name__ == "__main__":
    shopping_list = []  # Initialize the shopping_list array

    while True:
        display_menu()  # Call the display_menu function

        try:
            choice = int(input("Enter your choice (1-3): "))  # Validate input as a number
            if choice == 1:
                item = input("Enter an item to add: ")
                shopping_list.append(item)
                print(f"'{item}' added to the shopping list.")
            elif choice == 2:
                if shopping_list:
                    print("Shopping List:")
                    for i, item in enumerate(shopping_list, 1):
                        print(f"{i}. {item}")
                else:
                    print("Shopping list is empty.")
            elif choice == 3:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Error: Please enter a valid number.")
