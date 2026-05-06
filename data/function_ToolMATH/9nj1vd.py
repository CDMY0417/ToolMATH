def cis_to_complex_a(r: float, theta_deg: float) -> complex:
    import math
    theta_rad = math.radians(theta_deg)
    return complex(r * math.cos(theta_rad), r * math.sin(theta_rad))
