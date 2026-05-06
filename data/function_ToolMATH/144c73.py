def calculate_divisors_of_prime_power(prime: int, power: int):
    return [prime ** i for i in range(power + 1)]
