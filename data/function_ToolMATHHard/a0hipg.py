def term_from_mean_sequence(n: int):
    """Return a_n where S_n = n^2."""
    if n <= 0:
        raise ValueError("n must be positive.")
    return 2*n - 1
