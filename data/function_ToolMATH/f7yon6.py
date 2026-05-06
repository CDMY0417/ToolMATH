def two_digit_multiples(numbers: list[int]) -> list[int]:
    multiples = []
    for number in numbers:
        multiple = number
        while multiple < 100:
            if multiple >= 10:
                multiples.append(multiple)
            multiple += number
    return sorted(multiples)
