def digit_product(num: int) -> int:
    tens = num // 10
    ones = num % 10
    return tens * ones
