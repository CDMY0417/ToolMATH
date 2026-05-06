def scalar_multiply_b(scalar: float, vector: tuple[float, float, float]) -> tuple[float, float, float]:
    return tuple(scalar * component for component in vector)
