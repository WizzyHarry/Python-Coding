#!/usr/bin/env python3

import s5_functions as f


def main():
    f.get_requirements()
    user_input = f.get_user_input()





    n1, n2, operator = user_input

    f.print_selection_structures(n1, n2, operator)

if __name__ == "__main__":
    main()