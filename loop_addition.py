#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Sept 2021
# This program is a loop calculator (addition)


def main():
    # This function adds all numbers 1 to the given integer.
    loop_counter = 0
    total = 0

    # input
    user_input = input("Enter a positive integer: ")

    # process & output
    try:
        user_input = int(user_input)

        if user_input < 0:
            print("Invalid Input.")
        else:
            while loop_counter <= user_input:
                total += loop_counter
                loop_counter += 1
            print(
                "The sum of all the positive numbers from 1 to {0} is {1}.".format(
                    user_input, total
                )
            )
    except (Exception):
        print("Invalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
