def repetend_position_to_digit(n: int, repetend_length: int, numerator: int) -> int:
    remainder = numerator
    for i in range(1, n + 1):
        remainder = (remainder * 10) % repetend_length
        digit = (remainder * 10) // repetend_length
    return digit
