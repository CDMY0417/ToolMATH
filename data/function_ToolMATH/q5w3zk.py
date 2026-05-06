def determinant_3x3(matrix: list[list[float]]) -> float:
    a, b, c = matrix[0]
    submatrix1 = [[matrix[1][1], matrix[1][2]], [matrix[2][1], matrix[2][2]]]
    submatrix2 = [[matrix[1][0], matrix[1][2]], [matrix[2][0], matrix[2][2]]]
    submatrix3 = [[matrix[1][0], matrix[1][1]], [matrix[2][0], matrix[2][1]]]
    det_sub1 = submatrix1[0][0] * submatrix1[1][1] - submatrix1[0][1] * submatrix1[1][0]
    det_sub2 = submatrix2[0][0] * submatrix2[1][1] - submatrix2[0][1] * submatrix2[1][0]
    det_sub3 = submatrix3[0][0] * submatrix3[1][1] - submatrix3[0][1] * submatrix3[1][0]
    return a * det_sub1 - b * det_sub2 + c * det_sub3
