def power_mod_c(n: int, m: int) -> int:
    result = 1
    base = 2
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % m
        base = (base * base) % m
        n //= 2
    return result
