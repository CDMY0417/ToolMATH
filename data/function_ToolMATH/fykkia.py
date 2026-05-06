def units_digit_of_product_d(numbers: list[int]) -> int:
    units_digit = 1
    for number in numbers:
        units_digit = (units_digit * number) % 10
    return units_digit
