#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(len(sys.argv)):
            if i == 0:
                continue
            print("{} {}".format(i, sys.argv[i]))
