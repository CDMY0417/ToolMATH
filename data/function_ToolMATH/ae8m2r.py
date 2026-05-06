def factors_of_number(number: int):
    return [i for i in range(1, number + 1) if number % i == 0]
