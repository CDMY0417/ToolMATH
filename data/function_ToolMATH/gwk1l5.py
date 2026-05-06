def interval_exclusion(low: float, high: float, point: float):
    if low < point < high:
        return [(low, point), (point, high)]
    return [(low, high)]
