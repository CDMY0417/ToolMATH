def polynomial_degree_a(expression: str):
    if 'x' not in expression:
        return 0
    terms = expression.split('+')
    degrees = [term.count('x') for term in terms]
    return max(degrees)
