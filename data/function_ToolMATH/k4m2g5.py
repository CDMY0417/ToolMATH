def cos_angle_from_sides(side1: float, side2: float, opposite_side: float) -> float:
    return (side1**2 + side2**2 - opposite_side**2) / (2 * side1 * side2)
