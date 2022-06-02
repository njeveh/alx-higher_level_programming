#!/usr/bin/python3
import calculator1 as calc

a = 10
b = 5

if __name__ == "__main__":
    print(f"{a} + {b} = {calc.add(a, b)}")
    print(f"{a} - {b} = {calc.sub(a, b)}")
    print(f"{a} * {b} = {calc.mul(a, b)}")
    print(f"{a} / {b} = {calc.div(a, b)}")
