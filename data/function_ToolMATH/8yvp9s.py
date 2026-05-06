def cross_product_a(u: tuple[float, float, float], v: tuple[float, float, float]) -> tuple[float, float, float]:
    x = u[1]*v[2] - u[2]*v[1]
    y = u[2]*v[0] - u[0]*v[2]
    z = u[0]*v[1] - u[1]*v[0]
    return (x, y, z)
