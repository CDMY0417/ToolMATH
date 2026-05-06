def are_vectors_proportional_a(v: tuple, w: tuple) -> bool:
    if v[0] * w[1] == v[1] * w[0] and v[0] * w[2] == v[2] * w[0] and v[1] * w[2] == v[2] * w[1]:
        return True
    return False
