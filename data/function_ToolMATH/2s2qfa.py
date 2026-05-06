def total_new_cans(initial_cans: int, rate: int) -> int:
    total_cans = 0
    while initial_cans >= rate:
        new_cans = initial_cans // rate
        total_cans += new_cans
        initial_cans = new_cans
    return total_cans
