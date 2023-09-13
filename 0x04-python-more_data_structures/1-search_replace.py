#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # create a new list to store the new data
    created_list = []

    for ele in my_list:

        if ele == search:
            created_list.append(replace)
        else:
            created_list.append(ele)

    return created_list
