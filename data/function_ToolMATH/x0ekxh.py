def cross_product_d(v1: tuple[float, float, float], v2: tuple[float, float, float]) -> tuple[float, float, float]:
    ax, ay, az = v1
    bx, by, bz = v2
    return (ay * bz - az * by, az * bx - ax * bz, ax * by - ay * bx)
