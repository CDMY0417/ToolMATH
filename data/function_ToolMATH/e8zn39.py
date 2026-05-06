def length_of_minor_axis(b_squared: float) -> float:
    semiminor_axis_length = (b_squared ** 0.5)
    minor_axis_length = 2 * semiminor_axis_length
    return minor_axis_length
