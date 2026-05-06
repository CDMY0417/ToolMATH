def first_and_last_digit_product(digits: list[int]) -> int:
    if not digits:
        return 0
    return digits[0] * digits[-1]
