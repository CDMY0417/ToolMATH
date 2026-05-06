def doublings_to_reach_target(target_multiple: int) -> int:
    count = 0
    while target_multiple > 1:
        target_multiple //= 2
        count += 1
    return count
