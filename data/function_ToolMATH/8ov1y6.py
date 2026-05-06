def residues_of_remaining_numbers(n: int, modulo: int) -> list:
    remainder = n % modulo
    return [i % modulo for i in range(1, remainder + 1)]
