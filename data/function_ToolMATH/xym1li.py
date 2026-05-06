def vector_projection_b(vector_a: list, vector_v: list):
    v_magnitude_squared = sum(v_i ** 2 for v_i in vector_v)
    if v_magnitude_squared == 0:
        return [0] * len(vector_a)
    scalar = sum(a_i * v_i for a_i, v_i in zip(vector_a, vector_v)) / v_magnitude_squared
    return [scalar * v_i for v_i in vector_v]
