def pythagorean_theorem_w(side1: float, side2: float, is_hypotenuse: bool) -> float:
    if is_hypotenuse:
        return (side1 ** 2 + side2 ** 2) ** 0.5
    else:
        return (abs(side1 ** 2 - side2 ** 2)) ** 0.5
