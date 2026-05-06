def subtract_vectors(vector1: tuple, vector2: tuple) -> tuple:
    return tuple(x - y for x, y in zip(vector1, vector2))
