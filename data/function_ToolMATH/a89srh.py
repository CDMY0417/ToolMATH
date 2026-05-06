def pythagorean_relationship(side1: float, side2: float, hypotenuse: float) -> bool:
    return abs(side1**2 + side2**2 - hypotenuse**2) < 1e-9
