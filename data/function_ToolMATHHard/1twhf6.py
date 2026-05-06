def even_part_sum_at_two(p0, p1, pm1):
    """Return P(2)+P(-2) using even part of cubic."""
    if isinstance(p0, str) or isinstance(p1, str) or isinstance(pm1, str):
        return f"4*({p1}+{pm1})-6*{p0}"
    return 4*(p1 + pm1) - 6*p0
