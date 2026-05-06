def combine_like_terms(terms: list[str]) -> str:
    coefficients = {}
    constant = 0
    for term in terms:
        if 'x' in term:
            coefficient = int(term.replace('x', '') or '1')
            coefficients['x'] = coefficients.get('x', 0) + coefficient
        else:
            constant += int(term)
    simplified = []
    if 'x' in coefficients:
        simplified.append(f"{coefficients['x']}x")
    if constant != 0:
        simplified.append(str(constant))
    return ' + '.join(simplified)
