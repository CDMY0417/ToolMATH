def symmetric_factor_p_sum(a, b, c):
    """Return p(a,b,c)=a+b+c."""
    if isinstance(a, str) or isinstance(b, str) or isinstance(c, str):
        return f"{a}+{b}+{c}"
    return a + b + c
