def switch_digits_add(n: int, add_value: int) -> int:
    a = n // 10
    b = n % 10
    return 10 * b + a + add_value
