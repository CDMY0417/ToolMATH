def absolute_sum_le_constraint(x: float, y: float, constraint: float) -> bool:
    return abs(x + y) + abs(x - y) <= constraint
