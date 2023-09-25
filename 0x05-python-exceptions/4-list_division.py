#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """list_division

        Args:
            my_list_1:  integer or string
            my_list_2:  integer or string
            list_length:    length of both

        Return:
            a new list with all division
    """
    ret = []
    try:
        for item in range(list_length):
            if item >= len(my_list_1) or item >= len(my_list_2):
                raise IndexError("out of range")
            try:
                alist = float(my_list_1[item])
                blist = float(my_list_2[item])
                if blist == 0:
                    raise ZeroDivisionError("division by 0")
                divided_result = alist / blist
                ret.append(divided_result)
            except ValueError:
                ret.append(0)
                print("wrong type")
            except ZeroDivisionError:
                ret.append(0)
                print("division by 0")
    except IndexError:
        print("out of range")
    finally:
        return ret
