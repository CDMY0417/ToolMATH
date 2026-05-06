def number_of_sides_from_angle(interior_angle: float) -> float:
    exterior_angle = 180 - interior_angle
    return 360 / exterior_angle
