def calculate_number_of_groups(total: int, group_size: int) -> int:
    return (total + group_size - 1) // group_size
