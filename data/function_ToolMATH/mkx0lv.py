def units_digit_of_power_f(number: int, power: int, base: int) -> int:
    units_digit = number % base
    result_units_digit = (units_digit ** power) % base
    return result_units_digit
