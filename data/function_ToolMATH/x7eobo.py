def solve_linear_system_i(total_sum: float, xy_ratio: float):
    x = xy_ratio * (total_sum / (1 + xy_ratio))
    y = total_sum - x
    return x, y
