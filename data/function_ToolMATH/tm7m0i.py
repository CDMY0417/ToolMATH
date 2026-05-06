def remaining_central_angle(total_angle: float, known_angles: list[float]) -> float:
    remaining_angle = total_angle - sum(known_angles)
    return remaining_angle
