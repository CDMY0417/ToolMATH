def unique_sums_of_two_elements(elements: list[int], limit: int) -> set:
    unique_sums = set()
    for i in range(len(elements)):
        for j in range(i, len(elements)):
            sum_elements = elements[i] + elements[j]
            if sum_elements < limit:
                unique_sums.add(sum_elements)
    return unique_sums
