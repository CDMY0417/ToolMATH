def largest_prime_factor_d(n: int) -> int:
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    max_prime = -1
    for i in range(2, n + 1):
        while n % i == 0:
            max_prime = i
            n //= i
    return max_prime
