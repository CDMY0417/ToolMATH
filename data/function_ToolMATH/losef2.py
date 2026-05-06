def binomial_coefficient_be(n: int, k: int, known_values: dict):
    if (n, k) in known_values:
        return known_values[(n, k)]
    if (n, n-k) in known_values:
        return known_values[(n, n-k)]
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n-1, k-1, known_values) + binomial_coefficient(n-1, k, known_values)
