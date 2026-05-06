def product_of_complex_exponentials(angle1: float, angle2: float, angle3: float) -> complex:
    import cmath
    a = cmath.exp(complex(0, angle1))
    b = cmath.exp(complex(0, angle2))
    c = cmath.exp(complex(0, angle3))
    return a * b * c
