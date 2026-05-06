def compose_functions(c: float, x: float) -> float:
    inner = c * x / (2 * x + 3)
    return (c * inner) / (2 * inner + 3)
