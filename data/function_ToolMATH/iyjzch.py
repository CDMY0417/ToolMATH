def tangent_period_reduction(angle: int) -> int:
    angle = angle % 180
    if angle > 90:
        angle -= 180
    return angle
