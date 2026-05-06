def find_preimage_count(target_values: set, f_mapping: dict) -> int:
    count = 0
    for x, fx in f_mapping.items():
        if fx in target_values:
            count += 1
    return count
