def trapezoid_area_i(rectangle_width: float, rectangle_height: float, triangle_base: float, triangle_height: float) -> float:
    rect_area = rectangle_width * rectangle_height
    tri_area = 0.5 * triangle_base * triangle_height
    return rect_area + tri_area
