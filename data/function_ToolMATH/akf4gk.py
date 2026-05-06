def quartic_polynomial_multiplication(quad1: tuple[float, float, float], quad2: tuple[float, float, float]) -> tuple[float, float, float, float, float]:
    a1, b1, c1 = quad1
    a2, b2, c2 = quad2
    return (a1*a2, a1*b2 + b1*a2, a1*c2 + b1*b2 + c1*a2, b1*c2 + c1*b2, c1*c2)
