#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is {(int((number**2)**(1/2))%10)}")
