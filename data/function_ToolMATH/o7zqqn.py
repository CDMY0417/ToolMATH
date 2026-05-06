def calculate_range_a(value: float, percent_error: float) -> tuple:
    lower_bound = value - value * (percent_error / 100)
    upper_bound = value + value * (percent_error / 100)
    return lower_bound, upper_bound
