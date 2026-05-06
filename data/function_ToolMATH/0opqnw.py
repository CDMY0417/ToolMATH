def range_overlap(range1: tuple[int, int], range2: tuple[int, int]) -> list[int]:
    start = max(range1[0], range2[0])
    end = min(range1[1], range2[1])
    if start < end:
        return list(range(start, end))
    return []
