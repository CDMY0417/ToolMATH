def filter_integers_absolute_difference(integers: list[int], a: int, m: int) -> list[int]:
    return [x for x in integers if abs(x - a) > m]
