#!/usr/bin/env python3

def get_requirements():
    print("Calorie Percentage")
    print("Developer: Keith Faunce")
    print("\nProgram Requirements:\n"
          + "1. Find calories per grams of fat, carbs, and protien.\n"
          + "2. Calculate percentages.\n"
          + "3. Must be float data types.\n"
          + "4. Format, right-align numbers, and round to decimal places.\n")
    

def get_user_input():
    fat_grams = 0.0
    carb_grams = 0.0
    protien_grams = 0.0


    print("Input:")
    fat_grams = float(input("Enter total fat grams: "))
    carb_grams = float(input("Enter total carb grams: "))
    protien_grams = float(input("Enter total protien grams: "))

    return fat_grams, carb_grams, protien_grams


def calculate_calories(f_grams, c_grams, p_grams):
    total_calories = 0.0
    percent_fat = 0.0
    percent_carbs = 0.0
    percent_protien = 0.0


    calories_from_fat = f_grams * 9
    calories_from_carbs = c_grams * 4
    calories_from_protien = p_grams * 4
    total_calories = calories_from_fat + calories_from_carbs + calories_from_protien


    percent_fat = calories_from_fat / total_calories
    percent_carbs = calories_from_carbs / total_calories
    percent_protien = calories_from_protien / total_calories

    print("\nOutput:")
    print("{0:8} {1:>10} {2:>13}".format("Type", "Calories", "Percentage"))

    print("{0:8} {1:10,.2f} {2:13.2%}".format(
        "Fat", calories_from_fat, percent_fat))

    print("{0:8} {1:10,.2f} {2:13.2%}".format(
        "Fat", calories_from_carbs, percent_carbs))
    
    print("{0:8} {1:10,.2f} {2:13.2%}".format(
        "Fat", calories_from_protien, percent_protien))