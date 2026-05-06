def herons_formula_b(side1: float, side2: float, side3: float) -> float:
    s = (side1 + side2 + side3) / 2
    area_squared = s * (s - side1) * (s - side2) * (s - side3)
    return area_squared ** 0.5
