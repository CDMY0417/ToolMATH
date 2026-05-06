def is_less_than_b(digits1: list[int], digits2: list[int], base: int) -> bool:
    len1, len2 = len(digits1), len(digits2)
    if len1 != len2:
        return len1 < len2
    for d1, d2 in zip(digits1, digits2):
        if d1 != d2:
            return d1 < d2
    return False
