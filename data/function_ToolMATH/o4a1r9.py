def is_identity_scaled(matrix: list[list[int]], scalar: int) -> bool:
    identity = [[scalar if i == j else 0 for j in range(3)] for i in range(3)]
    return matrix == identity
