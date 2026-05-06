def inverse_as_linear_combo(M):
    # Solve a,b so that M^-1 = a M + b I for a 2x2 matrix M
    a,b,c,d = M[0][0], M[0][1], M[1][0], M[1][1]
    det = a*d - b*c
    if det == 0:
        raise ValueError('Matrix is singular')
    inv = [[d/det, -b/det], [-c/det, a/det]]
    # Solve for a,b using entries: inv = alpha*M + beta*I
    # Using off-diagonal entries
    if b != 0:
        alpha = inv[0][1] / b
    elif c != 0:
        alpha = inv[1][0] / c
    else:
        alpha = 0
    beta = inv[0][0] - alpha*a
    return [alpha, beta]
