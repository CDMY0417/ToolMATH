def round_to_nearest(number: float, place: int) -> float:
    factor = 10 ** place
    return round(number / factor) * factor
