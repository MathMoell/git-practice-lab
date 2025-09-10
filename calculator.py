import math

# Liitmine
def add(a, b):
    return a + b

# Lahutamine
def subtract(a, b):
    return a - b

# Korrutamine
def multiply(a, b):
    return a * b

# Jagamine
def divide(a, b):
    if b != 0:
        return a / b
    return 'Error: Division by zero'

# Jõud (exponent)
def power(a, b):
    return a ** b

# Modulo ehk jäägi leidmine
def mod(a, b):
    return a % b

# Ruutjuur (error käsitlemine negatiivsete arvudega)
def sqrt(a):
    if a >= 0:
        return math.sqrt(a)
    return 'Error: Negative number'

# Faktoriaali arvutamine
def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return 'Error: Negative number'
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Test print väljundi kuvamiseks
if __name__ == "__main__":
    print("Kalkulaator: 2 + 3 =", add(2, 3))
    print("Kalkulaator: 5 - 3 =", subtract(5, 3))
    print("Kalkulaator: 4 * 2 =", multiply(4, 2))
    print("Kalkulaator: 6 / 2 =", divide(6, 2))
    print("Kalkulaator: 2 ** 3 =", power(2, 3))
    print("Kalkulaator: 10 % 3 =", mod(10, 3))
    print("Kalkulaator: sqrt(16) =", sqrt(16))
    print("Kalkulaator: factorial(5) =", factorial(5))
    print("Kalkulaator: factorial(-1) =", factorial(-1))

