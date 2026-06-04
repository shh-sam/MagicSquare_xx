# D-* Logic Track 테스트 ID

| ID | 파일 | 검증 대상 |
|----|------|-----------|
| D-01 | `tests/test_d_constants.py` | MagicConstant SSOT (34, 16, 4, 0) |
| D-02 | `tests/test_d_line_sum.py` | 단일 줄 합 (행/열/대각) |
| D-03 | `tests/test_d_validate.py` | `ValidateAllLines` — 10선 전부 34 |
| D-04 | `tests/test_d_validate.py` | `ValidateAllLines` — 불일치 존재 |
| D-05 | `tests/test_d_report.py` | `ReportMismatchLines` — 전선 통과 → 빈 목록 |
| D-06 | `tests/test_d_report.py` | `ReportMismatchLines` — 단일 줄 불일치 (line_id, expected, actual) |
| D-07 | `tests/test_d_report.py` | `ReportMismatchLines` — 복수 줄 불일치 |
| D-08 | `tests/test_d_regression.py` | 동일 grid → 동일 출력 (AC-3) |
| D-LOC-01 | `tests/entity/test_d_loc_01.py` | `find_blank_coords(G1)` → `[(2,2),(3,3)]` 1-index · **GREEN PASS** |
| D-LOC-02 | `tests/entity/test_d_loc_02.py` | G1 → `len(result) == 2` (후속 RED) |
| D-LOC-03 | `tests/entity/test_d_loc_03.py` | G2 → `[(0,2),(2,3)]` 0-index (후속 RED) |

> U-* (UI Track): 후속 세션 — `tests/test_u_*.py`  
> Golden Master (D-LOC-01): `tests/golden/d_loc_01_g1_blank_coords.golden.json`  
> Golden Master (D-SOL-01): `tests/golden/d_sol_01_g1_step_a.approved.txt` · `tests/_approval.py`
