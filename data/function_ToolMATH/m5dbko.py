def sum_equations_a(equations: list[list[float]]) -> list[float]:
    return [sum(terms) for terms in zip(*equations)]
