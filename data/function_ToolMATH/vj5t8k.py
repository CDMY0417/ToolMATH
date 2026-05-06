def largest_prime_divisor(number: int) -> int:
    def is_prime(num: int) -> bool:
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    largest_prime = -1
    for i in range(2, number + 1):
        while number % i == 0:
            if is_prime(i):
                largest_prime = i
            number //= i
    return largest_prime
