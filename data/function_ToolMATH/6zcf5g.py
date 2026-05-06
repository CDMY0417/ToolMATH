def sin_periodicity(angle: int) -> int:
    equivalent_angle = angle % 360
    if equivalent_angle > 180:
        equivalent_angle -= 360
    return equivalent_angle if -90 <= equivalent_angle <= 90 else -(equivalent_angle - 180)
