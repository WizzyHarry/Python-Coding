#!/usr/bin/env python3

SQFT_PER_GALLON = 350  # Constant square feet per gallon

def get_requirements():
    print("Interior Paint Estimator")
    print("Developed by Keith Faunce")
    print("\nProgram Requirements:\n"
          "1. Calculate home interior paint cost (w/o primer).\n"
          "2. Must use float data types.\n"
          f"3. Must use {SQFT_PER_GALLON} constant for square feet per gallon.\n"
          "4. Must use iteration structure (loop).\n"
          "5. Format, right-align numbers, and round to two decimal places.\n"
          "6. Create at least five functions to be called by the program.\n"
            + "a. main(): calls two other functions: get_requirements() and estimate_painting_cost()\n"
            + "b. get_requirements(): displays the program requirements.\n"
            + "c. estimate_painting_cost(): calculates interior home painting, and calls print functions.\n"
            + "d. print_painting_estimate(): displays painting costs.\n"
            + "e. print_painting_percentage(): displays painting cost percentages.\n")


def get_user_input(): 
    # Input statements specifying float data types
    total_sq_ft = float(input("Enter total interior sq ft: "))
    price_per_gallon = float(input("Enter price per gallon paint: "))
    hourly_rate_per_sq_ft = float(input("Enter hourly painting rate per sq ft: "))
    
    return total_sq_ft, price_per_gallon, hourly_rate_per_sq_ft


def estimate_painting_cost(total_sq_ft, price_per_gallon, hourly_rate_per_sq_ft): 
    # Calculates variable data for print statements
    num_gallons = total_sq_ft / SQFT_PER_GALLON
    paint_cost = num_gallons * price_per_gallon
    labor_cost = total_sq_ft * hourly_rate_per_sq_ft
    total_cost = paint_cost + labor_cost
    
    return num_gallons, paint_cost, labor_cost, total_cost


def print_painting_estimate(total_sq_ft, num_gallons, paint_cost, labor_cost, total_cost, price_per_gallon, hourly_rate_per_sq_ft):
    # Print statements with formatting commands
    # Arranged in table esque view 
    print(f"\n{'Item':<20}{'Amount':>10}") 
    print(f"{'Total Sq Ft:':<20}{total_sq_ft:>10.2f}") 
    print(f"{'Sq Ft per Gallon:':<20}{SQFT_PER_GALLON:>10.2f}") 
    print(f"{'Number of Gallons:':<20}{num_gallons:>10.2f}")
    print(f"{'Paint per Gallon:':<20}{price_per_gallon:>10.2f}")
    print(f"{'Labor per Sq Ft:':<20}{hourly_rate_per_sq_ft:>10.2f}")
    
    # Print cost for job at hand
    print(f"\n{'Cost':<20}{'Amount':>10}")
    print(f"{'Paint:':<20}${paint_cost:>10.2f}") 
    print(f"{'Labor:':<20}${labor_cost:>10.2f}")
    print(f"{'Total:':<20}${total_cost:>10.2f}")


def print_painting_percentage(paint_cost, labor_cost, total_cost):
    # Print percentages to show cost share
    paint_percentage = (paint_cost / total_cost) * 100 
    labor_percentage = (labor_cost / total_cost) * 100
    print(f"\n{'Cost':<20}{'Percentage':>10}")
    print(f"{'Paint:':<20}{paint_percentage:>10.2f}%")
    print(f"{'Labor:':<20}{labor_percentage:>10.2f}%")
    print(f"{'Total:':<20}{100.00:>10.2f}%")
