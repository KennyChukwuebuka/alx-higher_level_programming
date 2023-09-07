#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5

    from calculator_1 import add
    from calculator_1 import sub
    from calculator_1 import mul
    from calculator_1 import div

    result = add(10, 5)
    result = sub(10, 5)
    result = mul(10, 5)
    result = div(10, 5)

    print('{} + {} = {}'.format(a, b, result))
    print('{} - {} = {}'.format(a, b, result))
    print('{} * {} = {}'.format(a, b, result))
    print('{} / {} = {}'.format(a, b, result))
