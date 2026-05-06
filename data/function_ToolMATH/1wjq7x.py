def find_numbers_in_interval(start: int, step: int, low: int, high: int) -> list[int]:
    numbers = []
    k = 0
    num = start + k * step
    while num <= high:
        if num >= low:
            numbers.append(num)
        k += 1
        num = start + k * step
    return numbers
