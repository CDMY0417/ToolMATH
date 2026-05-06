def projection_from_example(v, proj_v, u):
    # Compute projection of u onto the same line as proj_v
    # Projection onto line spanned by proj_v
    denom = proj_v[0]*proj_v[0] + proj_v[1]*proj_v[1]
    if denom == 0:
        raise ValueError('projection vector must be nonzero')
    dot = u[0]*proj_v[0] + u[1]*proj_v[1]
    scale = dot / denom
    return [scale*proj_v[0], scale*proj_v[1]]
