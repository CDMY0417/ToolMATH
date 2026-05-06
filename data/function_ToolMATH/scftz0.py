def least_prime_factor(number: int):
    if number <= 1:
        return None
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return i
    return number
