def filter_primes(numbers: list[int]) -> list[int]:
    def is_prime(num: int) -> bool:
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return [num for num in numbers if is_prime(num)]
