#!/usr/bin/python3

def uniq_add(my_list=[]):
    get_uniq_int = set()

    sum_of_uniq = 0

    for num in my_list:

        if num not in get_uniq_int:
            get_uniq_int.add(num)

            sum_of_uniq += num
    return sum_of_uniq
