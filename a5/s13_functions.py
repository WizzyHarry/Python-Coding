import math 

def get_requirements():
    print("Sphere Volume Program\n")
    print("Developed by Keith Faunce\n")
    print("\nProgram Requirements:\n"
          + "1. Program calculates sphere volume in liquid U.S. gallons from user-entered diameter value in inches, and rounds to two decimal places.\n"
          + "2. Must use Pythons built in PI and pow() capabilities.\n"
          + "3. Program checks for non-integers and non-numeric values.\n"
          + "4. Program continues to prompt for user entry until no longer requested, prompt accepts upper or lower case letters.")
    

def sphere_volume():
    diameter = 0
    volume = 0.0
    gallons = 0.0
    choice = ''

    print("Input:")

    choice = input("Do you want to calculate a sphere volume (y or n)?").lower()

    print("\nOutput:")


    while (choice[0] == 'y'):
        diameter = input("Please enter diameter in inches (integers only):")
        test = True
        while (test == True):
            try:
                diameter = int(diameter)

                volume = (4.0 / 3.0) * math.pi * math.pow(diameter / 2.0, 3)
                gallons = volume / 231
                print("\nSphere volume: {0:,.2f} liquid U.S. gallons\n".format(gallons))
                test = False
            
            except ValueError:
                print("\nNot valid integer!")
                diameter = input("Please enter diameter in inches: ")
            continue

        choice = input("Do you want to calculate another sphere volume?").lower()

    print("\nThank you for using our Sphere volume calculator!!")