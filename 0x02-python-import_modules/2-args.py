#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # get the c-line argument
    arguments = sys.argv[1:]

    num_of_arguments = len(arguments)
    # print number of arguments
    if num_of_arguments == 0:
        print("{} arguments.".format(num_of_arguments))
    elif num_of_arguments == 1:
        print("{} argument:".format(num_of_arguments))
    else:
        print("{} arguments:".format(num_of_arguments))
    # get the list of all arguments
    if num_of_arguments > 0:
        for i, num_of_arg in enumerate(arguments, start=1):
            print("{}: {}".format(i, num_of_arg))
