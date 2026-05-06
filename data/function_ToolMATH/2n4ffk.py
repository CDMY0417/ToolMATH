def solve_linear_equations(coefficients: list[list[float]], constants: list[float]):
    from sympy import Matrix
    augmented_matrix = Matrix(coefficients).row_join(Matrix(constants))
    reduced_matrix = augmented_matrix.rref()[0]
    return [reduced_matrix[i, -1] for i in range(reduced_matrix.rows)]
