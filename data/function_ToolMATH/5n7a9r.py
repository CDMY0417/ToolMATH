def least_number_congruent_mod_k(start: int, r: int, k: int) -> int:
    if start % k == r:
        return start
    return start + (r - start % k) % k
