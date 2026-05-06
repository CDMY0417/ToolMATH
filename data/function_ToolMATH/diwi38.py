def nth_root_of_unity(n: int, k: int) -> complex:
    import cmath
    return cmath.exp(2 * cmath.pi * k * 1j / n)
