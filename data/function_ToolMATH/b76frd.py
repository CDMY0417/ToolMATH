def gcd_of_two_numbers(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x
