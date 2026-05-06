def create_excluded_interval(exclude: float):
    return ((float('-inf'), exclude), (exclude, float('inf')))
