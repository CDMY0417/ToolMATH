def calculate_intersection(count_a: int, count_b: int, union_count: int) -> int:
    intersection = count_a + count_b - union_count
    return intersection
