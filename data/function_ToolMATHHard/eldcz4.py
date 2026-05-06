def count_rectangles_grid(rows: int, cols: int):
    # Count rectangles in a grid with rows x cols cells
    return (rows*(rows+1)//2) * (cols*(cols+1)//2)
