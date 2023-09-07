#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5

    import calculator_1

    result_add = calculator_1.add(10, 5)
    result_sub = calculator_1.sub(10, 5)
    result_mul = calculator_1.mul(10, 5)
    result_div = calculator_1.div(10, 5)

    print('{} + {} = {}'.format(a, b, result_add))
    print('{} - {} = {}'.format(a, b, result_sub))
    print('{} * {} = {}'.format(a, b, result_mul))
    print('{} / {} = {}'.format(a, b, result_div))
