#!/usr/bin/python3
for first_digit_number in range(10):
    for second_digit_number in range(first_digit_number + 1, 10):
        print("{:02d}, {:02d}".format(first_digit_number, second_digit_number),
              end=", " if second_digit_number < 9 else "\n")
