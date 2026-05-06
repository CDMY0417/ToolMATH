def solve_linear_map_from_two_vector_images(v1, v2, w1, w2):
    'Solve 2x2 matrix M such that M v1 = w1 and M v2 = w2.'
    a,b = v1
    c,d = v2
    det = a*d - b*c
    if det == 0:
        raise ValueError('v1 and v2 must be independent')
    m11 = (w1[0]*d - w2[0]*b) / det
    m12 = (-w1[0]*c + w2[0]*a) / det
    m21 = (w1[1]*d - w2[1]*b) / det
    m22 = (-w1[1]*c + w2[1]*a) / det
    return [[m11, m12],[m21, m22]]
