def factor_ratio_cubes(a, b, c):
    """Return (a+b)(a+c)(b+c)."""
    if isinstance(a, str) or isinstance(b, str) or isinstance(c, str):
        return f"({a}+{b})*({a}+{c})*({b}+{c})"
    return (a+b)*(a+c)*(b+c)
