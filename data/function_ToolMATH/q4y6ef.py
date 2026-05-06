def vector_projection_a(v: tuple, u: tuple):
    dot_product = v[0] * u[0] + v[1] * u[1]
    u_dot_u = u[0] * u[0] + u[1] * u[1]
    scalar = dot_product / u_dot_u
    return (scalar * u[0], scalar * u[1])
