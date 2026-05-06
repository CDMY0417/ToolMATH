def surface_area_of_exposed_cubes(cubes_added: int, surface_area_per_cube: int, missing_surface_area_per_cube: int):
    return cubes_added * (surface_area_per_cube - missing_surface_area_per_cube)
