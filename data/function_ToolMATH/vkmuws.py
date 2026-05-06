def largest_prime_with_digits(num_digits: int) -> int:
    import sympy
    start = 10**(num_digits - 1)
    end = 10**num_digits - 1
    for n in range(end, start - 1, -1):
        if sympy.isprime(n):
            return n
    return None
