def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)