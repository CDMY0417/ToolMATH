def sum_of_cubes_divisible_by(n: int, m: int) -> bool:
    return (n**3 + (m-n)**3) % m == 0
