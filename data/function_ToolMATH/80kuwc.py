def negative_reciprocal(slope: float) -> float:
    if slope == 0:
        return float('inf')
    else:
        return -1 / slope
