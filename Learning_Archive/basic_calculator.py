def a():
    while True:
        try:
            a = float(input("Enter the first number: "))
            return a
        except ValueError:
            print("\nInvalid value. Please try again!")

def b():
    while True:
        try:
            b = float(input("Enter the second number: "))
            return b
        except ValueError:
            print("\nInvalid value. Please try again!")

def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operator"

def startcalc():
    while True:
        consent = input("Do you want to continue with the calculator? (y/n): ").lower()
        if consent == 'y':
            num1 = a()
            operator = input("Enter the operator (+, -, *, /): ")
            num2 = b()
            result = calculate(num1, operator, num2)
            print(result)

            while isinstance(result, float):
                operator = input("Enter the operator (+, -, *, /): ")
                num2 = b()
                result = calculate(result, operator, num2)
                print(result)
            
            print("Cannot continue calculation with the previous result.")
            return False
            break  # Exit the loop if the result is not a float

        elif consent == 'n':
            print("Entering main frame...")
            return  # Exit startcalc and return to the main menu

        else:
            print("Invalid choice. Please try again!")

    return True  # Return True to indicate successful calculator usage
