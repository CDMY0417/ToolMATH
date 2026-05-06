def subtract_equations_g(equation1: list[float], equation2: list[float]) -> list[float]:
    return [c1 - c2 for c1, c2 in zip(equation1, equation2)]
