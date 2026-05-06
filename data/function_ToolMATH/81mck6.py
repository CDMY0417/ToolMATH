def integer_divide_by_two_until_one(number: int) -> int:
    count = 0
    while number > 1:
        number //= 2
        count += 1
    return count
