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
    i = 0
    new_result_list = []
    res = 0
    for i in range(0, list_length):
        try:
            res = (my_list_1[i] / my_list_2[i])
        except TypeError:
            res = 0
            print("wrong type")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            new_result_list.append(res)
    return new_result_list
