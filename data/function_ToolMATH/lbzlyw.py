def pythagorean_theorem_b(side1: int, side2: int, is_hypotenuse: bool):
    if is_hypotenuse:
        return (side1**2 + side2**2)**0.5
    else:
        return abs(side1**2 - side2**2)**0.5
