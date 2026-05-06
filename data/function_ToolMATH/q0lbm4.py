def complex_roots_of_unity(n: int):
    import cmath
    return [cmath.exp(2j * cmath.pi * k / n) for k in range(n)]
