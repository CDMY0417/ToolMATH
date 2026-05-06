def inverse_of_linear_function_b(a: float, b: float):
    def f_inv(y):
        return (y - b) / a
    return f_inv
