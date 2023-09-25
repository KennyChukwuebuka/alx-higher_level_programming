#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """safe_print_list - print list

    Args:
        my_list: items to print
        x: integer

    Return:
        Number of element printed
    """
    count = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end='')
            count += 1
    except IndexError:
        pass
    finally:
        print()
    return count
