def is_multiple_of_but_not_of_others(number: int, multiple: int, not_multiples: list[int]) -> bool:
    if number % multiple != 0:
        return False
    for not_multiple in not_multiples:
        if number % not_multiple == 0:
            return False
    return True
