def total_distance_after_bounces(initial_height: float, bounces: int) -> float:
    total_distance = initial_height
    current_height = initial_height
    for _ in range(bounces):
        current_height /= 2
        total_distance += 2 * current_height
    return total_distance
