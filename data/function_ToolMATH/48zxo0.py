def divisors_of_number_d(n: int):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return divisors
