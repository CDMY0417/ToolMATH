def triangle_inequality_range_a(side1: int, side2: int):
    lower_bound = abs(side1 - side2) + 1
    upper_bound = side1 + side2 - 1
    return range(lower_bound, upper_bound + 1)
