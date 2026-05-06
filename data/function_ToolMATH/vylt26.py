def solve_scaled_identity_system(scale: int, vector: list) -> list:
    return [[element / scale] for element in vector]
