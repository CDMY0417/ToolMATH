def compute_number_of_new_containers(num_old_containers: int, volume_old: float, volume_new: float) -> int:
    total_old_volume = num_old_containers * volume_old
    num_new_containers = total_old_volume / volume_new
    return int(num_new_containers)
