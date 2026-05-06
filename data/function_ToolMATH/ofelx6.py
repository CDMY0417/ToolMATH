def positive_root(numbers: tuple):
    for number in numbers:
        if number > 0:
            return number
    return None
