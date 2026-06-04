"""Shared fixtures — G1/G2 grid data only (no domain logic)."""

import pytest

from entity.constants import BLANK, GRID_SIZE, MAX_VALUE, TARGET_SUM


@pytest.fixture
def grid_g1() -> list[list[int]]:
    """G1: 4×4 partial magic square, 2 blanks, row-major."""
    grid = [
        [MAX_VALUE, 3, 2, 13],
        [5, BLANK, 11, 8],
        [9, 6, 7, 12],
        [4, BLANK, 14, 1],
    ]
    assert len(grid) == GRID_SIZE
    assert all(len(row) == GRID_SIZE for row in grid)
    assert sum(grid[0]) == TARGET_SUM
    return grid
