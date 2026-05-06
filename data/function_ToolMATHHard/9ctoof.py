def orthogonal_basis_coefficients(a, b, c, v):
    'Return coefficients of v in an orthogonal basis a,b,c.'
    def dot(u, w):
        return sum(ui*wi for ui, wi in zip(u, w))
    p = dot(v, a) / dot(a, a)
    q = dot(v, b) / dot(b, b)
    r = dot(v, c) / dot(c, c)
    return [p, q, r]
