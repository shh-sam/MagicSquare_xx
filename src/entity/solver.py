"""Partial magic square solver — Step A row-sum fill (1-index int[6] output)."""

from entity.constants import BLANK, GRID_SIZE, INDEX_OFFSET, TARGET_SUM
from entity.location import find_blank_coords


def solution(grid: list[list[int]]) -> list[int]:
    """Step A: fill blanks from row sums; return [r1,c1,n1,r2,c2,n2] (1-index)."""
    result: list[int] = []
    for row_1, col_1 in find_blank_coords(grid):
        row_0 = row_1 - INDEX_OFFSET
        col_0 = col_1 - INDEX_OFFSET
        row_total = sum(
            grid[row_0][col] if grid[row_0][col] != BLANK else 0
            for col in range(GRID_SIZE)
        )
        result.extend([row_1, col_1, TARGET_SUM - row_total])
    return result
