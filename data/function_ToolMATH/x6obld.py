def evaluate_fractional_inequality(x: float, offset: float, root1: float, root2: float):
    numerator = x + offset
    denominator = (x - root1) * (x - root2)
    return (numerator / denominator) <= 0
