def factorial_units_digit_a(n: int) -> int:
    if n >= 5:
        return 0
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product % 10
