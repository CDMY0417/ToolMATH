def maximum_error(list1: list[float], list2: list[float]) -> float:
    return max(abs(x - y) for x, y in zip(list1, list2))
