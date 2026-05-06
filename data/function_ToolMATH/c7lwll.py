def scalar_multiplication_matrix(scalar: float, dimension: int):
    return [[scalar if i == j else 0 for j in range(dimension)] for i in range(dimension)]
