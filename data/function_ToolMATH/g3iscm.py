def roots_of_unity_d(n: int):
    return [f'cis(2 * pi * {j} / {n})' for j in range(1, n)]
