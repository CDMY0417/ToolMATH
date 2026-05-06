def symmetric_factor_p(a, b, c):
    """Return p(a,b,c) = -(ab+ac+bc)."""
    # If inputs are strings, return symbolic string
    if isinstance(a, str) or isinstance(b, str) or isinstance(c, str):
        return f"-({a}*{b} + {a}*{c} + {b}*{c})"
    return -(a*b + a*c + b*c)
