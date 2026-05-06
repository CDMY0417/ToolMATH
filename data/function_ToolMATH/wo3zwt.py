def midpoint_of_vectors(u: list[float], v: list[float]) -> list[float]:
    return [(u_i + v_i) / 2 for u_i, v_i in zip(u, v)]
