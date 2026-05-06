def solve_k_for_coplanar_lines(p0, q0, v0, v1, w):
    'Solve k so that lines P0 + s*(v0 + k*v1) and Q0 + t*w are coplanar.'
    def cross(u, v):
        return [
            u[1]*v[2] - u[2]*v[1],
            u[2]*v[0] - u[0]*v[2],
            u[0]*v[1] - u[1]*v[0],
        ]
    def dot(u, v):
        return sum(ui*vi for ui, vi in zip(u, v))
    def add(u, v):
        return [ui+vi for ui, vi in zip(u, v)]

    d = [q0[i]-p0[i] for i in range(3)]
    f0 = dot(d, cross(v0, w))
    v0_plus_v1 = add(v0, v1)
    f1 = dot(d, cross(v0_plus_v1, w))

    if f1 == f0:
        if f0 == 0:
            return None
        raise ValueError('No solution for k')
    k = -f0 / (f1 - f0)
    return k
