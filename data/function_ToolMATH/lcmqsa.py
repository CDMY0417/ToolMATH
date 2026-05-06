def solve_cone_radius(volume: float, height: float) -> float:
    r_squared = (3 * volume) / (height * 3.14159)
    return r_squared ** 0.5
