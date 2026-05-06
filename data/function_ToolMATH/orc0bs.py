def min_power_of_ten_divisible(prime_factors: dict):
    twos = prime_factors.get(2, 0)
    fives = prime_factors.get(5, 0)
    return max(twos, fives)
