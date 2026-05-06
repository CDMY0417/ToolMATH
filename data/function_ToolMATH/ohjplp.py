def compute_fraction_product(offset: int, max_value: int) -> float:
    numerator = 1
    denominator = 1
    for n in range(1, max_value + 1):
        numerator *= (n + offset)
        denominator *= n
    return numerator / denominator
