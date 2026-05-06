def probability_last_digit_value(digits: list[int], value: int) -> float:
    count_value = digits.count(value)
    total_digits = len(digits)
    return count_value / total_digits
