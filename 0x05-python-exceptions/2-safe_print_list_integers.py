#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """safe_print_list_integers

    Args:
        my_list: contains integers and string
        x: number of element

    Return:
        integers
    """
    count = 0
    try:
        for i in my_list:
            if isinstance(i, int):
                value_to_format = "{:d}".format(i)
                print(value_to_format, end='')
                count += 1
                if count == x:
                    break
    except TypeError:
        pass
    except IndexError:
        pass
    finally:
        print()
    return count
