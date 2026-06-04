"""Test ID: D-SOL-01 — solution(G1) Step A success (int[6], 1-index)."""

from entity.solver import solution

from tests._approval import assert_matches_golden

GOLDEN_D_SOL_01_G1_STEP_A = "d_sol_01_g1_step_a.approved.txt"


def test_d_sol_01_step_a_success(grid_g1):
    # Given: G1 격자 (빈칸 2개)
    # When: solution(grid_g1) Step A
    # Then: int[6] Golden Master 일치
    result = solution(grid_g1)
    assert len(result) == 6
    assert_matches_golden(result, GOLDEN_D_SOL_01_G1_STEP_A)
