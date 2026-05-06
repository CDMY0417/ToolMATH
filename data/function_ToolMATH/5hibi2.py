def arc_length_ratio(angle1: float, circumference1: float, angle2: float, circumference2: float) -> float:
    length1 = (angle1 / 360) * circumference1
    length2 = (angle2 / 360) * circumference2
    return length1 / length2
