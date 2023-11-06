#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, div, mul
    argc = len(sys.argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    ch = sys.argv[2]
    b = int(sys.argv[3])
    if ch == "+":
        result = add(a, b)
    elif ch == "-":
        result = sub(a, b)
    elif ch == "*":
        result = mul(a, b)
    elif ch == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, ch, b, result))
