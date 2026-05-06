def sum_of_increments(lst: list[int], increment: int) -> int:
    return sum(x + increment for x in lst)
