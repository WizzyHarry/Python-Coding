#!/usr/bin/env python3


import s14_functions as f

def main():
    f.get_requirements()
    num1 = f.get_valid_float(1)
    num2 = f.get_valid_float(2)
    op = f.get_valid_operator()
    f.get_calculator(num1, num2, op)

if __name__ == "__main__":
    main()



"""
import s14_functions as f

def main():
    f.get_requirements()
    f.get_valid_float(pos)
    f.get_valid_operator()
    f.get_calculator()


if __name__ == "__main__":
    main()
"""