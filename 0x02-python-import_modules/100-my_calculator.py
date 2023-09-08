#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print('Usage: {} <a> <operator> <b>'.format(sys.argv[0]))
        sys.exit(1)

    a = int(sys.argv[1])
    sys_opr = sys.argv[2]
    b = int(sys.argv[3])

    if sys_opr == "+":
        res = add(a, b)
    elif sys_opr == "-":
        res = sub(a, b)
    elif sys_opr == "*":
        res = mul(a, b)
    elif sys_opr == "/":
        res = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print('{} {} {} = {}'.format(a, sys_opr, b, res))
