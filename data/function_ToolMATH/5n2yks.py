def divisors_a(number: int):
    divs = [i for i in range(1, number + 1) if number % i == 0]
    return divs
