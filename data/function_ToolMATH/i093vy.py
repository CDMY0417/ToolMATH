def tan_difference_identity(a: float, b: float) -> float:
    import math
    tan_a = math.tan(a)
    tan_b = math.tan(b)
    return (tan_a - tan_b) / (1 + tan_a * tan_b)
