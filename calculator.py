def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return 'Error: Division by zero'

def power(a, b):
    return a ** b

if __name__ == "__main__":
    print("Kalkulaator: 2 + 3 =", add(2, 3))

import math

def mod(a, b):
    return a % b

def sqrt(a):
    if a >= 0:
        return math.sqrt(a)
    return 'Error: Negative number'
