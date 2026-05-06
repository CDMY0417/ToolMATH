def ellipse_axes(a2: float, b2: float):
    semi_major_axis = max(a2, b2) ** 0.5
    semi_minor_axis = min(a2, b2) ** 0.5
    return (semi_major_axis, semi_minor_axis)
