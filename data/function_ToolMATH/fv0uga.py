def calculate_steps_ratio(person1_steps: int, person1_ratio: int, person2_steps: int, person2_ratio: int):
    scale_factor = person2_steps / person2_ratio
    equivalent_steps = person1_steps * scale_factor
    return equivalent_steps
