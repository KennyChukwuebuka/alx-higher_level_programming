#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """My delete function

    Args:
        my_list: first arg
        idx: second arg

        Returns:
            The copy of new list value
    """
    # check if the list is empty or if idx is out of range
    if not my_list or idx < 0 or idx >= len(my_list):
        return my_list

    my_list[:] = my_list[:idx] + my_list[idx+1:]
    return my_list
