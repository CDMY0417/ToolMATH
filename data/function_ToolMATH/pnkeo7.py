def pair_products_a(n: int) -> list[tuple[int, int]]:
    pairs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            pairs.append((i, n // i))
    return pairs
