def matrix_power_2x2(M, n: int):
    'Compute integer power n of a 2x2 matrix M.'
    if len(M) != 2 or any(len(row) != 2 for row in M):
        raise ValueError('M must be 2x2')
    if n < 0:
        raise ValueError('n must be nonnegative')
    def matmul(A, B):
        return [
            [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
        ]
    result = [[1,0],[0,1]]
    base = [row[:] for row in M]
    exp = n
    while exp > 0:
        if exp % 2 == 1:
            result = matmul(result, base)
        base = matmul(base, base)
        exp //= 2
    return result
