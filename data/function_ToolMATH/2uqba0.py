def is_four_digit_representation(number: int, base: int) -> bool:
    return base ** 3 <= number < base ** 4
