def smallest_n_for_probability_threshold(base_prob: float, threshold: float) -> int:
    n = 0
    while base_prob ** n >= threshold:
        n += 1
    return n
