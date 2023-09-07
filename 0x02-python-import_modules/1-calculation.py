#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5

    from calculator_1 import add
    from calculator_1 import sub
    from calculator_1 import mul
    from calculator_1 import div

    result_add = add(10, 5)
    result_sub = sub(10, 5)
    result_mul = mul(10, 5)
    result_div = div(10, 5)

    print('{} + {} = {}'.format(a, b, result_add))
    print('{} - {} = {}'.format(a, b, result_sub))
    print('{} * {} = {}'.format(a, b, result_mul))
    print('{} / {} = {}'.format(a, b, result_div))
