def cauchy_schwarz_inequality_b(u: list[float], v: list[float]) -> bool:
    assert len(u) == len(v), 'Lists must be of the same length'
    return sum(ui * vi for ui, vi in zip(u, v)) ** 2 <= sum(ui ** 2 for ui in u) * sum(vi ** 2 for vi in v)
