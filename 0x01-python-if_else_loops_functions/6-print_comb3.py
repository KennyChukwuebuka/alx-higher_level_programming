#!/usr/bin/python3
for first_digit_number in range(9):
    for second_digit_number in range(first_digit_number + 1, 10):
        print("{:d}{:d}".format(first_digit_number, second_digit_number),
              end=", " if first_digit_number != 8
              or second_digit_number != 9 else "\n")
