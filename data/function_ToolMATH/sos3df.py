def sum_of_first_n_primes(n: int) -> int:
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

    prime_sum = 0
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            prime_sum += num
            count += 1
        num += 1
    return prime_sum
