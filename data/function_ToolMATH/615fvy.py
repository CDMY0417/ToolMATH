def choose_distinct_digits(digit_choices: int, number_to_choose: int) -> int:
    result = 1
    for i in range(number_to_choose):
        result *= (digit_choices - i)
    return result
