def find_factors_c(number: int):
    factors = [i for i in range(1, number + 1) if number % i == 0]
    return factors
