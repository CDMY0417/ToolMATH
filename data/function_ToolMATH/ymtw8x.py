def calculate_remaining_angle_in_polygon(total_angle: float, known_angles: list[float]) -> float:
    return total_angle - sum(known_angles)
