def parameterize_line_through_vectors(start: tuple, end: tuple, t: float):
    return tuple(start_i + t * (end_i - start_i) for start_i, end_i in zip(start, end))
