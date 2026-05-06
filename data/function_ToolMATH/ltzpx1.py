def calculate_radius_from_area(area: float, pi_approx: float):
    r_squared = area / pi_approx
    return r_squared ** 0.5
