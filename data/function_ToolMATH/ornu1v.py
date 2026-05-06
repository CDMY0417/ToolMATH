def ellipse_axes_lengths_a(a_squared: float, b_squared: float):
    semimajor = max(a_squared, b_squared) ** 0.5
    semiminor = min(a_squared, b_squared) ** 0.5
    return semimajor, semiminor
