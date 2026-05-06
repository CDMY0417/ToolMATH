def side_ratios_30_60_90_triangle(shortest_side: float):
    long_side = shortest_side * 2
    middle_side = shortest_side * (3**0.5)
    return shortest_side, middle_side, long_side
