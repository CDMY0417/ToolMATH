def vector_triple_product_a(a: tuple, b: tuple, c: tuple) -> tuple:
    a_dot_c = sum(x * y for x, y in zip(a, c))
    a_dot_b = sum(x * y for x, y in zip(a, b))
    first_term = tuple(x * a_dot_c for x in b)
    second_term = tuple(x * a_dot_b for x in c)
    return tuple(x - y for x, y in zip(first_term, second_term))
