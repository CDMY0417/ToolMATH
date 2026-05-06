def two_digit_primes_less_than(limit: int):
    primes = []
    for num in range(10, limit):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes
