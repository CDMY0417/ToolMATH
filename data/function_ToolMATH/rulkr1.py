def identity_theorem_verify(f_values: tuple):
    return all(value == f_values[0] for value in f_values)
