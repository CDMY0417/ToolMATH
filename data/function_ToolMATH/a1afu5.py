def power_of_i_c(n: int):
    powers = [1, 1j, -1, -1j]
    return powers[n % 4]
