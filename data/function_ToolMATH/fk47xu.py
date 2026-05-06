def sum_of_two_dice(sides: int, target_sum: int):
    pairs = []
    for die1 in range(1, sides + 1):
        for die2 in range(1, sides + 1):
            if die1 + die2 == target_sum:
                pairs.append((die1, die2))
    return pairs
