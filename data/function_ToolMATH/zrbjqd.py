def cross_product_e(vector_a: tuple[float, float, float], vector_b: tuple[float, float, float]) -> tuple[float, float, float]:
    ax, ay, az = vector_a
    bx, by, bz = vector_b
    return (
        ay * bz - az * by,
        az * bx - ax * bz,
        ax * by - ay * bx
    )
