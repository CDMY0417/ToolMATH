def cross_product_b(u: tuple, v: tuple) -> tuple:
    cpx = u[1]*v[2] - u[2]*v[1]
    cpy = u[2]*v[0] - u[0]*v[2]
    cpz = u[0]*v[1] - u[1]*v[0]
    return (cpx, cpy, cpz)
