def primes_up_to_n_a(limit: int):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return [num for num in range(2, limit + 1) if is_prime(num)]
