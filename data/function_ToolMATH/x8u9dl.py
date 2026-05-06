def integers_with_remainder(start: int, end: int, divisor: int, remainder: int) -> int:
    count = 0
    for num in range(start, end + 1):
        if num % divisor == remainder:
            count += 1
    return count
