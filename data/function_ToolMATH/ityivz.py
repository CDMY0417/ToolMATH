def probability_odd_sum_given_even_product(dice_sides: int, dice_count: int) -> str:
    numerator = 2 * dice_count * (dice_sides // 2) ** (dice_count - 1)
    denominator = (dice_sides ** dice_count) - ((dice_sides // 2) ** dice_count)
    return f'{numerator}/{denominator}'
