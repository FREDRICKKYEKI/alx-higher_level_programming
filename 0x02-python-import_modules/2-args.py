#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(f"0 arguments.")
    else:
        print(f"{len(sys.argv) - 1} arguments:")
        for i in range(len(sys.argv)):
            if i == 0:
                continue
            print(f"{i} {sys.argv[i]}")
