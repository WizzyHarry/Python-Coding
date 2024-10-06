#!/usr/bin/env python3
def get_requirements():
    print("Pyhton Selection Structures")
    print("Developed by Keith Faunce")
    print("\nProgram Requirements:\n"
          + "1. Use Python selection structure.\n"
          + "2. Prompt user for two numbers, and a suitable operator.\n"
          + "3. Test for correct numeric operator.\n"
          + "4. Replicate display below.\n")
    
    print("Python Calculator")


def get_user_input():
    num1 = 0.0
    num2 = 0.0

    num1 = float(input("Enter num1: "))
    num2 = float(input("Enter num2: "))
    print("\nSuitable Operators: +,-,*,/, // (integer divison), % (modulo operator), ** (power)")
    op = input("Enter operator: ")

    return num1, num2, op


def print_selection_structures(num1, num2, op):
    if op == "+":
        print(num1 + num2)
    
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(num1 / num2)
    elif op == "//":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(num1 // num2)
    elif op == "%":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(num1 % num2)
    elif op == "**":
        print("Using ** operator: " + str(num1 ** num2))

        print("Using pow() function: " + str(pow(num1, num2)))
    else:
        print("Incorrect operator!")

        