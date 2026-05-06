def projection_from_example_2d(v, proj_v, u):
    # Project u onto same line as proj_v
    denom = proj_v[0]*proj_v[0] + proj_v[1]*proj_v[1]
    if denom == 0:
        raise ValueError('projection vector must be nonzero')
    dot = u[0]*proj_v[0] + u[1]*proj_v[1]
    scale = dot / denom
    return [scale*proj_v[0], scale*proj_v[1]]
