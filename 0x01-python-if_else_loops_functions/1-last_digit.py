#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(repr(number)[-1])
if last_digit == 0:
    print(f"Last digit of {number} is 0 ", end='')
    print("and is 0")

else:
    last_digit *= int((number/abs(number)))
    print(f"Last digit of {number} is {last_digit} ", end='')
    if last_digit > 5:
        print("and is greater than 5")
    elif last_digit < 6:
        print("and is less than 6 and not 0")
