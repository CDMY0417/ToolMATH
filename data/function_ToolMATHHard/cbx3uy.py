def inverse_zero_solution_for_reciprocal_linear(b):
    """Return the expression for x such that f^{-1}(x)=0 for f(x)=1/(a*x+b)."""
    # f(0) = 1/b, so the solution is x = 1/b
    if isinstance(b, (int, float)):
        if b == 0:
            raise ValueError("b must be nonzero.")
        return 1.0 / b
    return f"1/{b}"
