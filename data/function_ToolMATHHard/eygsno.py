def b_from_cubic_root_sum_sqrt(dummy: int = 0):
    """Return b using minimal polynomial of 2+sqrt(3) and rational coefficient constraint."""
    # Minimal polynomial: x^2 - 4x + 1. Third root r satisfies product = -10.
    # (2+sqrt3)(2-sqrt3)=1 so r=-10. Sum roots = (2+sqrt3)+(2-sqrt3)-10 = -6 => a=6.
    # b = sum pairwise products = 1 + (-10)(2+sqrt3) + (-10)(2-sqrt3) = 1 - 20 - 20 = -39.
    return -39
