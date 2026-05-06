def count_games_two_divisions(teams_per_division: int, num_divisions: int):
    """Return total number of games."""
    if num_divisions != 2:
        raise ValueError("This tool assumes 2 divisions.")
    n = teams_per_division
    intra = (n*(n-1)//2) * 2 * num_divisions
    inter = n*n
    return intra + inter
