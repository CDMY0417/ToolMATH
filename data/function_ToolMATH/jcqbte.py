def modular_congruences(r: int, m: int):
    x = r
    while True:
        yield x
        x += m
