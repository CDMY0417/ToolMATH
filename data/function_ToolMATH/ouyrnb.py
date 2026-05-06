def count_integers_within_modulo_class(limit: int, divisor: int, mods: list[int]) -> int:
    count = 0
    for n in range(1, limit + 1):
        if n % divisor in mods:
            count += 1
    return count
