def find_integer_solution_modulo(a: int, b: int, mod: int, upper_bound: int) -> int:
    for n in range(upper_bound):
        if (a * n) % mod == b % mod:
            return n
    return -1
