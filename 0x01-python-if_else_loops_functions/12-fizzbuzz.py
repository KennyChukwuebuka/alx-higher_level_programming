#!/usr/bin/python3
def fizzbuzz():
    for fiz_num in range(1, 101):
        if fiz_num % 3 == 0 and fiz_num % 5 == 0:
            print("FizzBuzz ", end="")
        elif fiz_num % 3 == 0:
            print("Fizz ", end="")
        elif fiz_num % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(fiz_num), end="")
