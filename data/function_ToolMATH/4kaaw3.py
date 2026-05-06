def pythagorean_theorem_a(leg: float, hypotenuse: float) -> float:
    missing_leg_squared = hypotenuse**2 - leg**2
    missing_leg = missing_leg_squared**0.5
    return missing_leg
