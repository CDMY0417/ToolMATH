def largest_power_of_base_less_than_or_equal(number: int, base: int) -> int:
    power = 1
    while power * base <= number:
        power *= base
    return power
