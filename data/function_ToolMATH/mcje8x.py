def gcd_of_two_numbers_a(x: int, y: int) -> int:
    while y != 0:
        x, y = y, x % y
    return x
