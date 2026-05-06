def possible_outcomes_of_linear(slope: int, intercept: int, excluded_x: int):
    excluded_value = slope * excluded_x + intercept
    return (-float('inf'), excluded_value), (excluded_value, float('inf'))
