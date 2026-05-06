def probability_roll_less_than_equal(target: int, die_outcomes: list[int]):
    successful_outcomes = sum(1 for outcome in die_outcomes if outcome <= target)
    return successful_outcomes / len(die_outcomes)
