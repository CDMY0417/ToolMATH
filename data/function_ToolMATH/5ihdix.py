def simplify_telescope_sum(n_terms: int) -> float:
    start = 1
    end = n_terms + 1
    return start - (1 / end)
