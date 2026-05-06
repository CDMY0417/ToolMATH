def weighted_average_a(size1: int, average1: float, size2: int, average2: float) -> float:
    total_score = (size1 * average1) + (size2 * average2)
    total_students = size1 + size2
    return total_score / total_students
