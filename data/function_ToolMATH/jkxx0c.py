def evaluate_even_function(f: dict, x: int):
    return f.get(x, f.get(-x))
