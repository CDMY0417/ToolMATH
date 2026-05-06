def a_over_b_from_proportional_rows(p1: float, q1: float, p2: float, q2: float):
    """Return a/b when (p2,q2)=k*(p1,q1), so b=k*a and a/b=1/k."""
    if p1 == 0 and q1 == 0:
        raise ValueError("First row must be nonzero.")
    if p1 != 0:
        k = p2 / p1
        if q1 * k != q2:
            raise ValueError("Rows are not proportional.")
    else:
        k = q2 / q1
        if p2 != 0:
            raise ValueError("Rows are not proportional.")
    if k == 0:
        raise ValueError("b is zero; a/b undefined.")
    return 1.0 / k
