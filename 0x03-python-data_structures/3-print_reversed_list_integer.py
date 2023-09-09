#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    reverse_number = reversed(my_list)
    for num in reverse_number:
        print("{}".format(num))
