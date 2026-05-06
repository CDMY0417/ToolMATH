def largest_prime_factor_e(n: int):
    def is_prime(num):
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
    largest_factor = -1
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            largest_factor = i
    return largest_factor
