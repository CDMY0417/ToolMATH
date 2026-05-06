def find_congruent_in_range(lower_bound: int, upper_bound: int, remainder: int, modulus: int):
    for num in range(lower_bound + 1, upper_bound + 1):
        if num % modulus == remainder:
            return num
    return None
