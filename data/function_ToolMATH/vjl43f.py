def roots_of_unity(n: int) -> list[complex]:
    from cmath import exp, pi
    return [exp(2j * pi * k / n) for k in range(n)]
