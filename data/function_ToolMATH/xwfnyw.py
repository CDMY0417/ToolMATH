def successful_outcomes_sum_to_target(sides: int, target_sum: int) -> int:
    count = 0
    for first_die in range(1, sides + 1):
        second_die = target_sum - first_die
        if 1 <= second_die <= sides:
            count += 1
    return count
