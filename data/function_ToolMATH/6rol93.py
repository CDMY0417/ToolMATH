def powers_of_i(n: int):
    cycle = [1, 1j, -1, -1j]
    return cycle[n % 4]
