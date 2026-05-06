def cross_product_3d_vectors(u: tuple[float, float, float], v: tuple[float, float, float]) -> tuple[float, float, float]:
    i = u[1] * v[2] - u[2] * v[1]
    j = u[2] * v[0] - u[0] * v[2]
    k = u[0] * v[1] - u[1] * v[0]
    return (i, j, k)
