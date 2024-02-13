def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def degree_of_five(numb):
    if numb <= 0:
        return False
    elif numb == 1:
        return True
    while numb % 5 == 0:
        numb /= 5
    return numb == 1