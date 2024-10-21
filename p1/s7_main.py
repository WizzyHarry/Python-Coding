#!/usr/bin/env python3
import s7_func as f


def main():
    f.get_requirements()
    list_size = f.user_input()
    f.using_lists(list_size)



if __name__ == "__main__":
    main()