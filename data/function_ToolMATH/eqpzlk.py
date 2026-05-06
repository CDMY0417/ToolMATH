def heron_formula_area(a: float, b: float, c: float) -> float:
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c))**0.5
