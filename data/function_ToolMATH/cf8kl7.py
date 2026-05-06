def check_contradiction(a1: int, b1: int, c1: int, a2: int, b2: int, c2: int) -> bool:
    if a1 == a2 and b1 == b2 and c1 != c2:
        return True
    return False
