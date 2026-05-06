def largest_prime_factor_b(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k <= 1:
            return False
        if k <= 3:
            return True
        if k % 2 == 0 or k % 3 == 0:
            return False
        i = 5
        while i * i <= k:
            if k % i == 0 or k % (i + 2) == 0:
                return False
            i += 6
        return True
    
    factor = 2
    largest = None
    while factor * factor <= n:
        if n % factor == 0:
            if is_prime(factor):
                largest = factor
            n //= factor
        else:
            factor += 1
    if n > 1 and is_prime(n):
        largest = n
    return largest
