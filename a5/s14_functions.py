def get_requirements():
    print("Calculator with Error Handling\n")
    print("Developed by Keith Faunce\n")
    print("\nProgram Requirements:\n"
          + "1. Program calculates two numbers, and rounds to two decimal places.\n"
          + "2. Prompt user for two numbers, and suitable operator.\n"
          + "3. Use Python error handling to validate data.\n"
          + "4. Test for correct arithmetic operator.\n"
          + "5. Division by zero not permitted.\n"
          + "6. Note: Program loops until correct input entered - numbers and arithmetic operator.\n")
    

def get_valid_float(pos):
    """Function tests for valid number. Accepts calling arg, number position (1 or 2)"""
    while True:
        try:
            num = float(input(f"\nEnter num{pos}: "))
            return num
        except ValueError:
            print("Not a valid number!")


def get_valid_operator():
    """Function tests for valid operator"""
    print("\nSuitable Operators: +, -, *, /, // (integer division), % (modulo operator), ** (power)")
    op_list = ['+', '-', '*', '/', '//', '%', '**']

    while True:
        op_test = input("Enter operator: ")
        if op_test in op_list:
            return op_test
        else:
            print("Incorrect operator!")


def get_calculator(num1, num2, op):
    if op == "+":
        print("{0:,.2f}".format(num1 + num2))
    elif op == "-":
        print("{0:,.2f}".format(num1 - num2))
    elif op == "*":
        print("{0:,.2f}".format(num1 * num2))
    elif op == "/":
        while True:
            try:
                print("{0:,.2f}".format(num1 / num2))
                break
            except ZeroDivisionError:
                print("Cannot divide by zero!")
                num2 = get_valid_float(2)
    elif op == "//":
        while True:
            try:
                print("{0:,.2f}".format(num1 // num2))
                break
            except ZeroDivisionError:
                print("Cannot divide by zero!")
                num2 = get_valid_float(2)
    elif op == "%":
        while True:
            try:
                print("{0:,.2f}".format(num1 % num2))
                break
            except ZeroDivisionError:
                print("Cannot divide by zero!")
                num2 = get_valid_float(2)
    elif op == "**":
        print("{0:,.2f}".format(num1 ** num2))



"""
def get_requirements():
    print("Calculator with Error Handling\n")
    print("Developed by Keith Faunce\n")
    print("\nProgram Requirements:\n"
          + "1. Program calculates two numbers, and rounds to two decimal places.\n"
          + "2. Prompt user for two numbers, and suitable operator.\n"
          + "3. Use Python error handling to validate data.\n"
          + "4. Test for correct arithmetic operator.\n"
          + "5. Division by zero no permitted.\n"
          + "6. Note: Program loops until correct input entered -numbers and arithmetic operator.\n")
    

def get_valid_float(pos):
    function tests for valid number. Accepts calling arg, number position (1 or 2)
    while True:
        try:
            num = float(input("\nEnter num" + str(pos) + ":"))
            return num 
            break # vs doesn't like

        except ValueError:
            print("Not valid number!")
            continue


def get_valid_operator():
    functions tests for valid operator
    print("\nSuitable Operators: +,-,*,/,// (integer division), % (modulo operator), ** (power)")
    op_list = ['+','-','*','/','//','%','**']
    op_test = input("Enter operator: ")


    while True:
        if op_test in op_list:
            return op_test
            break # vs doesn't like

        else:
            print("Incorrect operator!")
            op_test = input("\nEnter operator.")
            continue



def get_calculator():
    num1 = 0.0
    num2 = 0.0
    op = ''


    num1 = get_valid_float(1)
    num2 = get_valid_float(2)
    op = get_valid_operator()

    if op == "+":
        print("{0:,.2f}".format(num1 + num2))

    elif op == "-":
        print("{0:,.2f}".format(num1 - num2))

    elif op == "*":
        print("{0:,.2f}".format(num1 * num2))

    elif op == "/":
        while True:
            try:
                print("{0:,.2f}".format(num1 / num2))
                break

            except ZeroDivisionError as err:
                print("Cannot divide by zero!")
                num2 = get_valid_float(2)
                continue

    elif op == "//":
        while True:
            try:
                print("{0:,.2f}".format(num1 // num2))
                break

            except ZeroDivisionError as err:
                print("Cannot divide by zero!")
                num2 = get_valid_float(2)
                continue

    elif op == "%":
        while True:
            try:
                print("{0:,.2f}".format(num1 % num2))
                break

            except ZeroDivisionError as err:
                print("Cannot divide by zero!")
                num2 = get_valid_float(2)
                continue

    elif op == "**":
        print("{0:,.2f}".format(num1 ** num2))
        print("{0:,.2f}".format(pow(num1, num2)))
"""