def count_numbers_with_digit_range(n: int, start_digit_min: int, start_digit_max: int, other_digits_min: int, other_digits_max: int) -> int:
    return (start_digit_max - start_digit_min + 1) * ((other_digits_max - other_digits_min + 1) ** (n - 1))
