def combine_like_terms_a(polynomial_terms: dict[int, int]) -> dict[int, int]:
    from collections import defaultdict
    combined_terms = defaultdict(int)
    for terms in polynomial_terms.values():
        for power, coefficient in terms.items():
            combined_terms[power] += coefficient
    return dict(combined_terms)
