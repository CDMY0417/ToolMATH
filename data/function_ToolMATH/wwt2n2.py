def find_periodic_digit(non_repeating: str, repeating: str, n: int):
    if n <= len(non_repeating):
        return int(non_repeating[n-1])
    else:
        index_in_repeating = (n - len(non_repeating) - 1) % len(repeating)
        return int(repeating[index_in_repeating])
