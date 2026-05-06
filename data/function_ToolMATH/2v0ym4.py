def next_prime_greater_than(number: int):
    def is_prime(x: int):
        if x <= 1:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    candidate = number + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate
