#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    first = int(sys.argv[1])
    second = int(sys.argv[3])
    opp = sys.argv[2]
    if opp == "+":
        print("{} + {} = {}".format(first, second, add(first, second)))
    elif opp == "-":
        print("{} - {} = {}".format(first, second, sub(first, second)))
    elif opp == "*":
        print("{} * {} = {}".format(first, second, mul(first, second)))
    elif opp == "/":
        print("{} / {} = {}".format(first, second, div(first, second)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
