def scalar_multiply_vector_b(scalar: int, vector: tuple) -> tuple:
    return tuple(scalar * x for x in vector)
