def adjacent_side_from_sin(opposite_side: float, hypotenuse_length: float) -> float:
    adjacent = (hypotenuse_length**2 - opposite_side**2)**0.5
    return adjacent
