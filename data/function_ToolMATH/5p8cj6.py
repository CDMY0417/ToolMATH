def ellipse_foci(center: tuple, semimajor_axis: int, semiminor_axis: int):
    c = (semimajor_axis**2 - semiminor_axis**2)**0.5
    x_center, y_center = center
    return ((x_center - c, y_center), (x_center + c, y_center))
