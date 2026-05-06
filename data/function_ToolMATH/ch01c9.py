def count_pairs_with_distance_less_than(distances: list[float], threshold: float) -> int:
    return sum(distance < threshold for distance in distances)
