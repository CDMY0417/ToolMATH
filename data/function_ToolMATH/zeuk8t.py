def cancel_opposites(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        if -number in numbers:
            numbers.remove(-number)
        else:
            total += number
    return total
