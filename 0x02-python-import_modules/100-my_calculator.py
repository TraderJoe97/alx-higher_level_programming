#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    count = len(sys.argv) - 1
    if count != 3:
        print("Usage: ./100-mycalculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    if operator == "+":
        print(f"{a} + {b} = {add(a, b)}")
    elif operator == "-":
        print(f"{a} - {b} = {sub(a, b)}")
    elif operator == "*":
        print(f"{a} * {b} = {mul(a, b)}")
    elif operator == "/":
        print(f"{a} / {b} = {div(a, b)}")
    else:
        print("Unknown opperator. Available operators: +, -, *, and /")
        sys.exit(1)
