def angle_shift(initial_angle: float, shifts: list[float]):
    return [(initial_angle + shift) % 360 for shift in shifts]
