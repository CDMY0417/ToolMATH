def binary_representation_length(number: int) -> int:
    length = 0
    while number > 0:
        number //= 2
        length += 1
    return length
