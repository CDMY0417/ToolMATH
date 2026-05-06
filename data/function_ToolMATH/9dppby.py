def power_of_i(n: int) -> complex:
    cycle = [1, 1j, -1, -1j]
    return cycle[n % 4]
