def non_invertible_modulo_integers(modulo: int) -> list:
    return [i for i in range(modulo) if i % 2 == 0]
