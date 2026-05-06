def fibonacci_modulo_period(modulo: int):
    a, b = 1, 1
    sequence = [a % modulo, b % modulo]
    while True:
        a, b = b, (a + b) % modulo
        if (a % modulo, b % modulo) == (1, 1):
            break
        sequence.append(b % modulo)
    return sequence
