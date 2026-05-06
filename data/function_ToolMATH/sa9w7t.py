def convert_base_and_digit_count_interval(digits: int, base: int):
    lower_bound = base ** (digits - 1)
    upper_bound = base ** digits
    return lower_bound, upper_bound
