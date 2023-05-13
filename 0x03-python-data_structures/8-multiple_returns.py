#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)

    if length != 0:
        fch = sentence[0]
        tup = (length, fch)

    else:
        tup = (length, None)
    return (tup)
