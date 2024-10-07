#!/usr/bin/env python3

import paint_functions as f

def main():
    f.get_requirements()
    
    while True:
        # Input for painting variables
        total_sq_ft, price_per_gallon, hourly_rate_per_sq_ft = f.get_user_input()
        
        # Estimate painting costs
        num_gallons, paint_cost, labor_cost, total_cost = f.estimate_painting_cost(total_sq_ft, price_per_gallon, hourly_rate_per_sq_ft)
        
        # Print statements for estimations & percentages
        f.print_painting_estimate(total_sq_ft, num_gallons, paint_cost, labor_cost, total_cost, price_per_gallon, hourly_rate_per_sq_ft)
        f.print_painting_percentage(paint_cost, labor_cost, total_cost)
        
        # End loop through user input
        if input("Estimate another paint job? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
