def tetrahedron_volume_with_inradius(area_abc: float, area_abd: float, area_acd: float, area_bcd: float, r: float) -> float:
    return (area_abc + area_abd + area_acd + area_bcd) * r / 3
