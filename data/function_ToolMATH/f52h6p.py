def factorial_units_digit_b(n: int) -> int:
    if n in (0, 1):
        return 1
    digits = [1, 1, 2, 6, 4]
    if n < 5:
        return digits[n]
    else:
        return 0
