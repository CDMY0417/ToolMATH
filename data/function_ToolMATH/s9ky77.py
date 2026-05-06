def harmonic_series_sum(a_values: list[float]) -> float:
    return sum(1 - a_i for a_i in a_values)
