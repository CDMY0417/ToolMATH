import math

def unit_vector_with_angle_bisected_by_b(a, b):
    'Compute unit vector v so that b bisects the angle between a and v.'
    def dot(u, w):
        return sum(ui*wi for ui, wi in zip(u, w))
    def norm(u):
        return math.sqrt(dot(u, u))
    na = norm(a)
    if na == 0:
        raise ValueError('a must be nonzero')
    a_hat = [ai/na for ai in a]
    bb = dot(b, b)
    ba = dot(b, a_hat)
    if ba == 0:
        raise ValueError('b must not be orthogonal to a')
    k = bb / (2 * ba)
    v = [b[i]/k - a_hat[i] for i in range(3)]
    nv = norm(v)
    return [vi/nv for vi in v]
