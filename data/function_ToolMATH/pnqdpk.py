def satisfies_triangle_inequality(length1: int, length2: int, length3: int) -> bool:
    length1, length2, length3 = sorted([length1, length2, length3])
    return length1 + length2 > length3
