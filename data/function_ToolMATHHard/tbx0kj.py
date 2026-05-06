def scale_line_to_y_coefficient(A: float, B: float, C: float, target_B: float):
    """Return scaled [A,B,C] with B=target_B."""
    if B == 0:
        raise ValueError("B must be nonzero.")
    scale = target_B / B
    return [A*scale, B*scale, C*scale]
