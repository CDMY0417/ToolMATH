def sum_values_at_keys(data: dict, keys: list[str]) -> int:
    return sum(data.get(key, 0) for key in keys)
