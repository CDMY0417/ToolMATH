def subtract_equations_a(a1: str, b1: str, total1: int, a2: str, b2: str, total2: int):
    resulting_var = a1 if a1 == a2 else b1
    return resulting_var, total1 - total2
