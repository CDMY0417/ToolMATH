from itertools import permutations

def count_numbers_with_permutation_multiple(start: int, end: int, divisor: int):
    """Return count of numbers whose digit permutation hits a multiple of divisor within range."""
    if start > end:
        raise ValueError("start must be <= end.")
    count = 0
    for n in range(start, end + 1):
        s = str(n)
        ok = False
        for p in set(permutations(s, len(s))):
            if p[0] == '0':
                continue
            m = int(''.join(p))
            if start <= m <= end and m % divisor == 0:
                ok = True
                break
        if ok:
            count += 1
    return count
