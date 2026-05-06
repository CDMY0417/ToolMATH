def apply_2d_transformation(matrix: list[list[float]], vector: list[float]) -> list[float]:
    x, y = vector
    transformed_x = matrix[0][0] * x + matrix[0][1] * y
    transformed_y = matrix[1][0] * x + matrix[1][1] * y
    return [transformed_x, transformed_y]
