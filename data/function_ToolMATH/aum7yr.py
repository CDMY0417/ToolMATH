def qm_am_inequality(x: float, y: float, z: float) -> bool:
    return ((x**2 + y**2 + z**2) / 3)**0.5 >= (x + y + z) / 3
