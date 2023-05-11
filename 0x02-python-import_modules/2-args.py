#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc < 2:
        print("0 arguments.")
    else:
        print("{} arguments:".format((argc - 1)))
        for i in range(argc):
            if i == 0:
                continue
            print("{} {}".format(i, sys.argv[i]))
