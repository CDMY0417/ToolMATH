def compute_composite_function(x: float, lambda_val: float):
    fx = lambda_val * x * (1 - x)
    return lambda_val * fx * (1 - fx)
