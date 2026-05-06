def count_perfect_cubes_in_range(lo: int, hi: int) -> int:
    count = 0
    n = 1
    while n**3 < lo:
        n += 1
    while n**3 <= hi:
        count += 1
        n += 1
    return count
