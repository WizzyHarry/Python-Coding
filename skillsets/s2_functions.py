#!/usr/bin/env3

def guidelines():
    print("Miles Per Gallon")

    print("Developer: Keith Faunce")
    print("\nProgram Requirements: \n"
          + "1. Convert MPG.\n"
          + "2. Must use float data type for user input and calculatuon.\n"
          + "3. Format and round conversion to two decimal places.")
    

def miles():
    mile = 0.0
    mile = float(input("\nEnter miles driven: "))
    gas = 0.0
    gas = float(input("\nEnter gallons of fuel used: "))

    travel = round(mile / gas, 2)

    print(f"\n{mile} miles driven and {gas} gallons used = {travel} miles per gallon")

