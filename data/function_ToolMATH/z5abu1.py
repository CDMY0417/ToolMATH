def count_perfect_square_factors_b(power1: int, power2: int) -> int:
    num_m_values = power1 // 2 + 1
    num_n_values = power2 // 2 + 1
    return num_m_values * num_n_values
