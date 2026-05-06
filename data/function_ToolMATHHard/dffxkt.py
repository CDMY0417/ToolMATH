def intersection_x_for_equal_shifted_parabolas(h1: float, h2: float):
    """Return x where (x-h1)^2 = (x-h2)^2 for h1!=h2."""
    if h1 == h2:
        raise ValueError("Parabolas coincide; infinite intersections.")
    return (h1 + h2) / 2.0
