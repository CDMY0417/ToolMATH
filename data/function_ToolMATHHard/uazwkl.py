def projection_of_vector(v, u):
    'Project vector v onto vector u.'
    dot = v[0]*u[0] + v[1]*u[1]
    uu = u[0]*u[0] + u[1]*u[1]
    if uu == 0:
        raise ValueError('u must be nonzero')
    scale = dot / uu
    return [scale * u[0], scale * u[1]]
