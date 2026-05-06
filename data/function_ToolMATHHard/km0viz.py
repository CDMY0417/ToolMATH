def reflect_over_vector(v, u):
    dot = v[0]*u[0] + v[1]*u[1]
    uu = u[0]*u[0] + u[1]*u[1]
    proj = [dot/uu*u[0], dot/uu*u[1]]
    return [2*proj[0]-v[0], 2*proj[1]-v[1]]
