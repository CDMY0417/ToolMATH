def find_coefficient(polynomial: str, term_degree: int) -> int:
    terms = polynomial.split("+")
    for term in terms:
        if f'x^{term_degree}' in term:
            coefficient = term.replace(f'x^{term_degree}', '').strip()
            return int(coefficient) if coefficient else 1
    return 0
