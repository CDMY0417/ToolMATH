def nth_decimal_digit(num: int, den: int, n: int):
    """Return nth digit after decimal point."""
    rem = num % den
    digit = 0
    for _ in range(n):
        rem *= 10
        digit = rem // den
        rem %= den
    return digit
