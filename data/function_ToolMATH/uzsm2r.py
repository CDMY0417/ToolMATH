def calculate_vertex_d_coordinates(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> tuple[int, int]:
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    d_x = c[0] - dx
    d_y = c[1] - dy
    return (d_x, d_y)
