def expand_cubic_difference(a: float, b: float) -> bool:
    return (a - b) * (a**2 + a*b + b**2) == a**3 - b**3
