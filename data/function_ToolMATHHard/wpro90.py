def inverse_as_linear_combo_2x2(M):
    a,b,c,d = M[0][0], M[0][1], M[1][0], M[1][1]
    det = a*d - b*c
    inv = [[d/det, -b/det], [-c/det, a/det]]
    # solve a,b using off-diagonal
    if b != 0:
        alpha = inv[0][1] / b
    else:
        alpha = inv[1][0] / c
    beta = inv[0][0] - alpha*a
    return [alpha, beta]
