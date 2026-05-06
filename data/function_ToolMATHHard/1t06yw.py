import math

def probability_same_color_two_draws_with_replacement(counts):
    """Return [num, den] for probability of same color with replacement."""
    total = sum(counts)
    if total == 0:
        raise ValueError("Total must be positive.")
    num = sum(c*c for c in counts)
    den = total * total
    g = math.gcd(num, den)
    return [num // g, den // g]
