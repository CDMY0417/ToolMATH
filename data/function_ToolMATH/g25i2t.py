def weighted_point_on_segment(a: int, b: int):
    total = a + b
    t = b / total
    u = a / total
    return (t, u)
