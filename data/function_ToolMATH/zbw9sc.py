def normalize_vector_a(x: int, y: int, z: int) -> tuple:
    magnitude = (x**2 + y**2 + z**2)**0.5
    return (x / magnitude, y / magnitude, z / magnitude)
