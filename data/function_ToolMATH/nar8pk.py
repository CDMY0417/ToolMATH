def quadratic_roots_complex(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    real_part = -b / (2*a)
    imaginary_part = (abs(discriminant)**0.5) / (2*a)
    return (real_part, imaginary_part)
