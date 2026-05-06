def dot_linear_combination(ab: float, bc: float, k1: float, k2: float):
    # Compute b · (k1 c + k2 a) given dot products a·b and b·c
    return k1*bc + k2*ab
