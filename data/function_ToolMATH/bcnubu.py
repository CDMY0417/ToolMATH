def factorial_units_digit(n: int) -> int:
    if n >= 5:
        return 0
    units_digit = 1
    for i in range(1, n + 1):
        units_digit = (units_digit * i) % 10
    return units_digit
