def solve_vector_from_cross_constraints(a, b):
    'Solve v such that v x a = b x a and v x b = a x b.'
    def dot(u, w):
        return sum(ui*wi for ui, wi in zip(u, w))
    aa = dot(a, a)
    ab = dot(a, b)
    bb = dot(b, b)
    A11, A12 = aa, -ab
    A21, A22 = ab, -bb
    B1 = aa - ab
    B2 = ab - bb
    det = A11*A22 - A12*A21
    if det == 0:
        raise ValueError('No unique solution')
    t = (B1*A22 - B2*A12) / det
    return [b[i] + t * a[i] for i in range(3)]
