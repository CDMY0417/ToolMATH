def calculate_missing_side(ab: float, bc: float, xy: float) -> float:
    yz = (bc * xy) / ab
    return yz
