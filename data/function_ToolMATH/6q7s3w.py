from cmath import exp, pi

def generate_nth_roots_of_unity(n: int) -> list:
    return [exp(2j * pi * k / n) for k in range(n)]
