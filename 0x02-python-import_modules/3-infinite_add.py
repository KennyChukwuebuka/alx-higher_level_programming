#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument = sys.argv[1:]
    arg_val = 0

    for arg in argument:
        arg_val += int(arg)
    print("{}".format(arg_val))
