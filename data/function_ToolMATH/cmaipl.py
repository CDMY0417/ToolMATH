def convert_to_polar_a(x: float, y: float):
    import cmath
    r = cmath.sqrt(x**2 + y**2).real
    theta = cmath.phase(complex(x, y))
    return r, theta
