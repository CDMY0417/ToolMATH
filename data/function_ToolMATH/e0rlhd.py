def mod_equivalence(a: int, b: int) -> int:
    return a % b if a % b >= 0 else (a % b) + b
