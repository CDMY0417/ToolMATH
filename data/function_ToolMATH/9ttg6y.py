def sum_units_digit_a(n: int) -> int:
    sum_total = n * (n + 1) // 2
    return sum_total % 10
