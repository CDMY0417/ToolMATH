def product_of_units_and_tens(number: int) -> int:
    units_digit = number % 10
    tens_digit = (number // 10) % 10
    return units_digit * tens_digit
