#!/usr/bin/env python3


def get_requirements():
    print("\nPython Lists\n")
    print("Developed by Keith Faunce\n")
    print("\nProgram Requirements:\n"
          + "1. Lists (Python data structure): mutable, ordered sequence of elements.\n"
          + "2. Lists are mutable/changeable--that is, can insert, update, delete.\n"
          + "3. Create list - using square brackets [list]: my_list = [cherries, apples, bananas, oranges].\n"
          + "4. Create a program that mirrors the following IPO format.\n")

def user_input():
    """Function to get user input"""
    while True:
        try:
            num = int(input("Enter number of list elements: "))
            return num
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def using_lists(num):
    """Function to create, modify, and display a list based on user input"""
    my_list = []

    # Gathering user input for the list
    for i in range(num):
        my_element = input("Please enter list element " + str(i + 1) + ": ")
        my_list.append(my_element)

    # Output section (moved outside of the loop)
    print("\nOutput:")
    print("Initial list:")
    print(my_list)

    # Insert element into a specific position
    elem = input("\nPlease enter an element to insert: ")
    while True:
        try:
            pos = int(input("Please enter the position index to insert at: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid index.")
    
    my_list.insert(pos, elem)
    print("\nList after inserting element:")
    print(my_list)

    # Count the number of elements in the list
    print("\nNumber of elements in the list:", len(my_list))

    # Sort the list alphabetically
    print("\nSorted list:")
    my_list.sort()
    print(my_list)

    # Reverse the list
    print("\nReversed list:")
    my_list.reverse()
    print(my_list)

    # Remove the last element
    print("\nList after removing the last element:")
    my_list.pop()
    print(my_list)

    # Delete the second element by index
    print("\nList after deleting the second element by index:")
    if len(my_list) > 1:
        del my_list[1]
    print(my_list)

    # Delete element by value ("cherries")
    if "cherries" in my_list:
        print("\nList after removing 'cherries':")
        my_list.remove("cherries")
    else:
        print("\n'Cherries' not found in the list.")
    print(my_list)

    # Clear all elements from the list
    print("\nClearing all elements from the list:")
    my_list.clear()
    print(my_list)

def main():
    """Main function to run the program"""
    get_requirements()
    num = user_input()
    using_lists(num)

if __name__ == "__main__":
    main()
