def calculate_time_for_bales(initial_horses: int, initial_bales: int, initial_time: int, target_horses: int, target_bales: int) -> int:
    time_for_target_horses = (initial_horses / target_horses) * initial_time
    time_for_target_bales = (target_bales / initial_bales) * time_for_target_horses
    return int(time_for_target_bales)
