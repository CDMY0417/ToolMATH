def triangle_inequality_holds(a: float, b: float) -> bool:
    return (abs(a + b) / (abs(a) + abs(b))) <= 1
