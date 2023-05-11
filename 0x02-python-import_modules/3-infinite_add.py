#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s = 0
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        s = s + int(sys.argv[i])
    print(s)
