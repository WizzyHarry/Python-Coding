#!/usr/bin/env python3

def guidelines():
    print("IT/ICT Student Percentage")
    print("Developed by Keith Faunce")
    print("\nProgram Requirements:\n"
          + "1. Find Number of IT/ICT students in class.\n"
          + "2. Calculate IT/ICT Student Percentage.\n"
          + "3. Must use float data type (to facilitate right-alignment).\n"
          + "4. Format, right-align numbers, and round to two decimal places.\n")
    

def student_body():
    it_students = 0.0
    it_students = float(input("Enter number of IT students: "))
    ict_students = 0.0
    ict_students = float(input("Enter number of ICT students: "))

    total = round(it_students + ict_students, 2)
    it_perc = round(it_students / total, 2) * 100
    ict_perc = round(ict_students / total, 2) * 100


    print("Output:\n")
    print(f"Total Students:   {total}")
    print(f"IT Students:      {it_perc}%")
    print(f"ICT Students:     {ict_perc}%")