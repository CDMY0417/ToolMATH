def total_descent_distance(initial_height: float, drops: int):
    total_distance = 0
    current_height = initial_height
    for _ in range(drops):
        total_distance += current_height
        current_height /= 2
    return total_distance
