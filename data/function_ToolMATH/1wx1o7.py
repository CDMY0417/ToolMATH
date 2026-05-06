def possible_sum_from_square(sum_of_squares: int) -> list:
    if sum_of_squares < 0:
        return []
    sqrt_value = int(sum_of_squares ** 0.5)
    return [sqrt_value, -sqrt_value] if sqrt_value * sqrt_value == sum_of_squares else []
