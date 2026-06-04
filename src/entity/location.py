"""Blank cell location queries (1-index coordinates)."""

from entity.constants import BLANK, GRID_SIZE, INDEX_OFFSET


def find_blank_coords(grid: list[list[int]]) -> list[tuple[int, int]]:
    """Return blank cell coordinates as (row, col) in 1-index, row-major order."""
    coords: list[tuple[int, int]] = []
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == BLANK:
                coords.append((row + INDEX_OFFSET, col + INDEX_OFFSET))
    return coords
