def collect_like_terms(coefficients: list[int], variables: list[str]):
    from collections import defaultdict
    term_dict = defaultdict(int)
    for coeff, var in zip(coefficients, variables):
        term_dict[var] += coeff
    return term_dict
