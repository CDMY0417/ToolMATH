def sum_of_powers(bases: list[int], exp: int) -> int:
    return sum(base ** exp for base in bases)
