def vector_projection(v: tuple, u: tuple) -> tuple:
    dot_product = v[0] * u[0] + v[1] * u[1]
    magnitude_squared = u[0]**2 + u[1]**2
    scalar = dot_product / magnitude_squared
    return (scalar * u[0], scalar * u[1])
