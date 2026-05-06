def power_of_i_a(n: int):
    powers = [1j, -1, -1j, 1]
    return powers[n % 4]
