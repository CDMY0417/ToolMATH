def triangle_inequality_range_b(side1: int, side2: int) -> list:
    start = abs(side1 - side2) + 1
    end = side1 + side2
    return list(range(start, end))
