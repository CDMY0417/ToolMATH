def evaluate_mixed_base_expression_with_division(a_str: str, a_base: int, b_str: str, b_base: int, c_str: str, c_base: int, d_str: str, d_base: int):
    """Return a/b - c + d with each term interpreted in its base."""
    a = int(a_str, a_base)
    b = int(b_str, b_base)
    c = int(c_str, c_base)
    d = int(d_str, d_base)
    return a / b - c + d
