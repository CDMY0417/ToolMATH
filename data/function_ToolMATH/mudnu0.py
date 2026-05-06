def largest_prime_factor_a(number: int) -> int:
    def is_prime(x: int) -> bool:
        if x <= 1:
            return False
        if x <= 3:
            return True
        if x % 2 == 0 or x % 3 == 0:
            return False
        i = 5
        while i * i <= x:
            if x % i == 0 or x % (i + 2) == 0:
                return False
            i += 6
        return True

    max_prime = -1
    for i in range(2, int(number ** 0.5) + 1):
        while number % i == 0:
            max_prime = i
            number //= i
    if number > 2:
        max_prime = number
    return max_prime
