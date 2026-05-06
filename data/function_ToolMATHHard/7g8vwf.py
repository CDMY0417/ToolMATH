import math

def left_matrix_from_product_2x2(target, right):
    (a,b),(c,d) = right
    det = a*d - b*c
    if det == 0:
        raise ValueError('Singular right matrix')
    inv = [[d/det, -b/det], [-c/det, a/det]]
    # multiply target * inv
    res = [
        [target[0][0]*inv[0][0] + target[0][1]*inv[1][0], target[0][0]*inv[0][1] + target[0][1]*inv[1][1]],
        [target[1][0]*inv[0][0] + target[1][1]*inv[1][0], target[1][0]*inv[0][1] + target[1][1]*inv[1][1]],
    ]
    return [[int(v) if abs(v-round(v))<1e-9 else v for v in row] for row in res]
