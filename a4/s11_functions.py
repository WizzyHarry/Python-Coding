#!/usr/bin/env python3
import random


def get_requirements():
    print("Psudeo-Random Number Generator\n")
    print("Developed by Keith Faunce\n")
    print("\nProgram Requirements:\n"
          + "1. Get user beginning and ending integer values, and store in two variables.\n"
          + "2. Display 10 pseudo-random numbers between, and including above values."
          + "3. Must use integer data types.\n"
          + "4. Example 1: Using range() and randint() functions.\n"
          + "5. Example 2: Using a list with range() and shuffle() functions.")
    

def random_numbers():
    """function prints psuedo-random numbers"""
    start = 0
    end = 0

    print("Input: ")
    start = int(input("Enter beginning value: "))
    end = int(input("Enter ending value: "))

    my_sequence = range(6)
    for item in my_sequence:
        print(item)

    print("\nOutput:")
    print("Example 1: Using range() and randint() functions.")

    for item in range(10):
        print(random.randint(start, end), sep=", ", end=" ")

    print()


    print("\nExample 2: Using a list, with a range() and shuffle() functions.")
    my_list = list(range(start, end +1))
    random.shuffle(my_list)
    for item in my_list:
        print(item, sep=", ", end=" ")


    print()
