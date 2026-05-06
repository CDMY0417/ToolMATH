def binomial_coefficient_ev(n: int, k: int):
    def factorial(x: int):
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result
    return factorial(n) // (factorial(k) * factorial(n - k))
