def sector_circumference_to_circle_circumference(circle_circumference: float, sector_angle: float, full_angle: float = 360.0) -> float:
    return (sector_angle / full_angle) * circle_circumference
