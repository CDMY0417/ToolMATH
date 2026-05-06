def max_of_parabolic_expression(c: int) -> int:
    vertex_x = c / 2
    return int(vertex_x * (c - vertex_x))
