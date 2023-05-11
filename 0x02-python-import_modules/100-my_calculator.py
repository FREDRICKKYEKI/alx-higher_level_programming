#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys
    args = sys.argv
    if len(args) > 1:
        a = int(args[1])
        b = int(args[3])
        op = args[2]
        match op:
            case '+':
                print("{} + {} = {}".format(a, b, calc.add(a, b)))
            case '-':
                print("{} + {} = {}".format(a, b, calc.sub(a, b)))
            case '*':
                print("{} + {} = {}".format(a, b, calc.mul(a, b)))
            case '/':
                print("{} + {} = {}".format(a, b, calc.div(a, b)))
            case _:
                print("Unknown operator. Available operators: +, -, * and /")
                sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
