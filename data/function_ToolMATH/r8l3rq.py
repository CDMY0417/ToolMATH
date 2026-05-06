def point_closer_to_center_than_vertices(point: tuple, center: tuple, vertices: list) -> bool:
    center_dist = (point[0] - center[0])**2 + (point[1] - center[1])**2
    for vertex in vertices:
        vertex_dist = (point[0] - vertex[0])**2 + (point[1] - vertex[1])**2
        if center_dist >= vertex_dist:
            return False
    return True
