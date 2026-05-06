def cosine_sine_expression_maximum(a: float, b: float) -> float:
    if a == 0 and b == 0:
        return 0.0
    else:
        return (a**2 + b**2)**0.5
