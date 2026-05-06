def solve_y_from_projection(v, w, k: float):
    # projection = (v·w)/(w·w) w = k w -> v·w = k (w·w)
    # v = (2,y,-5)
    dot = k * (w[0]*w[0] + w[1]*w[1] + w[2]*w[2])
    y = (dot - v[0]*w[0] - v[2]*w[2]) / w[1]
    return y
