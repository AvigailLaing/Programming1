import math


def display_menu():
    print("\nCalculator Menu")
    print("---------------")
    print("0. Exit Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Logarithm")
    print("7. Display Average")


# Initialize variables
result = 0.0
total_sum = 0.0
num_calculations = 0
print("Current Result:", result)

# Display the menu once before entering the loop
display_menu()

# Loop until user chooses to exit
while True:
    try:
        # Ensure the "Enter Menu Selection" is on a new line
        selection = int(input("\nEnter Menu Selection: "))

        if selection == 0:
            print("Thanks for using this calculator. Goodbye!")
            break
        elif selection == 7:
            if num_calculations == 0:
                print("Error: No calculations yet to average!")
                # Do not show the full menu, just prompt for the next selection
                continue
            else:
                average = total_sum / num_calculations
                print(f"Sum of calculations: {total_sum}")
                print(f"Number of calculations: {num_calculations}")
                print(f"Average of calculations: {average:.2f}")
                continue
        elif selection in [1, 2, 3, 4, 5, 6]:
            operand1 = input("Enter first operand: ")
            if operand1 == "RESULT":
                operand1 = result
            else:
                operand1 = float(operand1)

            operand2 = input("Enter second operand: ")
            if operand2 == "RESULT":
                operand2 = result
            else:
                operand2 = float(operand2)

            # Perform operations based on the menu selection
            if selection == 1:
                result = operand1 + operand2
            elif selection == 2:
                result = operand1 - operand2
            elif selection == 3:
                result = operand1 * operand2
            elif selection == 4:
                if operand2 != 0:
                    result = operand1 / operand2
                else:
                    print("Error: Invalid input!")
                    continue
            elif selection == 5:
                if operand1 == 0 and operand2 < 0:
                    print("Error: Invalid input!")
                    continue
                elif operand1 < 0 and operand2 % 1 != 0:
                    print("Error: Invalid input!")
                    continue
                else:
                    result = operand1 ** operand2
            elif selection == 6:
                if operand1 > 0 and operand1 != 1 and operand2 > 0:
                    result = math.log(operand2, operand1)
                else:
                    print("Error: Invalid input!")
                    continue

            # Update total and count of calculations
            total_sum += result
            num_calculations += 1
            print("Current Result:", result)
        else:
            # Invalid selection, only prompt for the next input without reprinting the menu
            print("Error: Invalid selection!")
            continue

        # Show the full menu again unless option 7 was selected with no previous calculations
        display_menu()

    except ValueError:
        print("Error: Invalid input!")