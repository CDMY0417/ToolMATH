def isolate_vector(a_vector: tuple, b_vector: tuple, ratio_a: int, ratio_b: int):
    t = -ratio_b / (ratio_a + ratio_b)
    u = ratio_a / (ratio_a + ratio_b)
    return (t, u)
