def count_odds_in_range(start: int, end: int) -> int:
    count = 0
    for i in range(start + (start % 2 == 0), end + 1, 2):
        count += 1
    return count
