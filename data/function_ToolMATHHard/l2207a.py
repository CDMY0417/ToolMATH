def inverse_matrix_3x3(M):
    # Compute inverse of a 3x3 matrix
    if len(M) != 3 or any(len(row) != 3 for row in M):
        raise ValueError('M must be 3x3')
    a,b,c = M[0]
    d,e,f = M[1]
    g,h,i = M[2]
    det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
    if det == 0:
        raise ValueError('Matrix is singular')
    adj = [
        [ (e*i - f*h), -(b*i - c*h),  (b*f - c*e)],
        [-(d*i - f*g),  (a*i - c*g), -(a*f - c*d)],
        [ (d*h - e*g), -(a*h - b*g),  (a*e - b*d)],
    ]
    return [[adj[r][c] / det for c in range(3)] for r in range(3)]
