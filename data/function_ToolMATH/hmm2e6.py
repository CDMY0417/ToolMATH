def calculate_smallest_digit_to_make_sum_divisible(current_sum: int, divisor: int) -> int:
    additional = divisor - (current_sum % divisor)
    return additional if additional < 10 else 10
