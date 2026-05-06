def square_radical_conjugates(m: int, n: int):
    x_squared = m + n + 2 * (m * n) ** 0.5
    y_squared = m + n - 2 * (m * n) ** 0.5
    return x_squared, y_squared
