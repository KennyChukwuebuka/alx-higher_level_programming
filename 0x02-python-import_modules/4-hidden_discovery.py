#!/usr/bin/python3
import importlib

values = importlib.import_module('hidden_4')
check = dir(values)
for name in check:
    if name[0] != '_':
        print(name)
