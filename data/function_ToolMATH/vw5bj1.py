def cube_complex_number(x: int, y: int):
    real_part = x**3 - 3*x*y**2
    imaginary_part = 3*x**2*y - y**3
    return real_part, imaginary_part
