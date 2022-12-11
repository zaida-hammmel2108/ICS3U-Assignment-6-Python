#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Nov 2022
# This program determines the perimeter of a decagon


def calculate_perimeter(int_side):

    if int_side <= 0 :
        perimeter = float(-1)
        return perimeter
    else:
        perimeter = float(int_side * 10)
        return perimeter



def main():
    # input
    str_side = input("Enter a side of the decagon (cm):")

    try:
        str_side = float(str_side)
        # call functions
        perimeter = calculate_perimeter(str_side)
        if perimeter == -1:
            print("That is an invalid input.")
        else:
            print("The perimeter of the decagon is: {0} cm.".format(perimeter))
    except ValueError:
        print("That is an invalid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
