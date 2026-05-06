def solve_for_overlap_time(probability: float, total_time: int):
    import math
    complement_probability = 1 - probability
    overlap_length = math.sqrt(complement_probability * (total_time ** 2))
    return total_time - overlap_length
