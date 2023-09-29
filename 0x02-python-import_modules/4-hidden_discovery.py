#!/usr/bin/python3
if __name__ != "__main___":

    import importlib

    file_imp = importlib.import_module('hidden_4')
    dir_loc = dir(file_imp)

    for name in dir_loc:
        if name[0] != '_':
            print(name)
