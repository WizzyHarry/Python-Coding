#!/usr/bin/env pyhton3

def guidelines():
    print("Square Feet to Acres")

    print("Developer: Keith Faunce")
    print("\nProgram Requirements: \n"
          + "1. Research: number of square feet to acre of land.\n"
          + "2. Must use float data type for user input and calculation.\n"
          + "3. Format and round conversion to two decimal places.\n")
    



  
def acre():
    acre = float(43560)
    sq_feet = 0
    sq_feet = float(input("Enter square feet: "))
    acres = sq_feet / acre
    return round(acres, 2)
    
