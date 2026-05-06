def product_of_primes(n: int) -> int:
    def is_prime(num: int) -> bool:
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    product, count, candidate = 1, 0, 2
    while count < n:
        if is_prime(candidate):
            product *= candidate
            count += 1
        candidate += 1
    return product
