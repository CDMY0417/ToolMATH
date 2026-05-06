def digit_count_condition(number: int, base: int, digit_count: int) -> bool:
    return base**digit_count > number and number >= base**(digit_count - 1)
