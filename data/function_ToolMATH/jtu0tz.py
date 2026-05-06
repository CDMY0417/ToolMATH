def generate_binary_outcomes(n: int) -> list[str]:
    from itertools import product
    return [''.join(seq) for seq in product('HT', repeat=n)]
