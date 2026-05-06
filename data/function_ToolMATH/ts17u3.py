def absolute_value_piecewise(x: float) -> float:
    if x < 1:
        return 4 - 2 * x
    elif 1 <= x < 3:
        return 4
    else:
        return 2 * x - 4
