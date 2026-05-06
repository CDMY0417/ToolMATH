def relative_speed(speed_a: float, speed_b: float, direction_same: bool):
    return abs(speed_a - speed_b) if direction_same else speed_a + speed_b
