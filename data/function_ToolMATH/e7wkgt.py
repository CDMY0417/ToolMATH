def convert_to_vertex_form_a(a: float, b: float, c: float) -> float:
    h = b / (2 * a)
    k = c - a * (h ** 2)
    return k
