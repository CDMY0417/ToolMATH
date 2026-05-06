def correct_units_digit_for_divisibility(base_sum: int, divisor: int) -> int:
    required_sum = (base_sum // divisor + 1) * divisor
    return required_sum - base_sum
