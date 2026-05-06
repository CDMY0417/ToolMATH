def transform_xz(x: float, z: float) -> tuple:
    x_1 = (x + z) / 3
    z_1 = (2 * x + 2 * z) / 3
    return x_1, z_1
