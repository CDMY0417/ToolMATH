def generate_equation_sequence(total_terms: int, extra_shift: int):
    return [n + extra_shift for n in range(1, total_terms + 1)]
