#!/usr/bin/env python3
import s4_functions as f


def main():
    f.get_requirements()
    user_input = f.get_user_input()



    fat, carb, protien = user_input

    f.calculate_calories(fat, carb, protien)


if __name__ == "__main__":
    main()