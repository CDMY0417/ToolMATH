def weighted_average_b(size1: int, average1: float, size2: int, average2: float) -> float:
    total_sum = size1 * average1 + size2 * average2
    total_size = size1 + size2
    return total_sum / total_size
