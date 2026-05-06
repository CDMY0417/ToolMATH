def compute_n_value(a: int, b: int) -> int:
    sqrt_a = int(a ** 0.5)
    sqrt_b = int(b ** 0.5)
    return (sqrt_a - sqrt_b) ** 2
