def find_smallest_divisible_by_k(numbers: list[int], k: int) -> int:
    for number in numbers:
        if number % k == 0:
            return number
    return None
