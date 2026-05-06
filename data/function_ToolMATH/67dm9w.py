def calculate_space_diagonal(width: float, height: float, length: float) -> float:
    base_diagonal = (width**2 + length**2)**0.5
    return (height**2 + base_diagonal**2)**0.5
