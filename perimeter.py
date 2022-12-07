#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Nov 2022
# This program determines the perimeter of a decagon


def perimeter_decagon(int_side):

    # process
    perimeter = 10 * int_side

    # output
    print("The perimeter is: {0} cm.".format(perimeter))


def main():
    # input
    str_side = input("Enter a side of the decagon: ")

    try:
        int_side = int(str_side)
        # call functions
        perimeter_decagon(int_side)
    except ValueError:
        print("Invalid integer.")

    print("\nDone.")


if __name__ == "__main__":
    main()
