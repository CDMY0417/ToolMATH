def positive_multiples_less_than_n(multiple: int, limit: int):
    return [multiple * i for i in range(1, limit // multiple + 1)]
