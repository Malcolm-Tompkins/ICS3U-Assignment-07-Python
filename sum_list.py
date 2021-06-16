#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on June 16, 2021
# Calculates the sum of any user input


def sum_list(number_list):
    sum_var = 0
    for valid_input in number_list:
        sum_var = sum_var + valid_input
    return sum_var


def main():
    number_list = []
    print("Enter your numbers one at a time, enter 'STOP' to stop")
    while True:
        user_input = (input("Enter your number: "))
        try:
            valid_input = int(user_input)
            number_list.append(valid_input)
        except Exception:
            if user_input == "STOP":
                print("Succesfully stopped")
                break
            else:
                print("{} is not a valid input".format(user_input))
                break
    sum_list(number_list)
    final_sum = sum_list(number_list)
    print("{} is the sum of your numbers".format(final_sum))
    print("Done.")


if __name__ == "__main__":
    main()
