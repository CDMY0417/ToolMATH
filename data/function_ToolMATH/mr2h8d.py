def positive_factors_a(number: int):
    return [i for i in range(1, number + 1) if number % i == 0]
