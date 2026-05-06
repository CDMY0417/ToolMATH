def remove_power_of_two(number: int) -> int:
    while number % 2 == 0:
        number //= 2
    return number
