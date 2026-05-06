def sum_geometric_series_d(first_term: float, common_ratio: float) -> float:
    assert 0 <= common_ratio < 1, 'Common ratio must be between 0 and 1'
    return first_term / (1 - common_ratio)
