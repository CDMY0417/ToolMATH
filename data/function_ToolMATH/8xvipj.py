def is_composite(number: int) -> bool:
    if number < 4:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return True
    return False
