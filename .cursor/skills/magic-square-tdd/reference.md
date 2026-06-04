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

> U-* (UI Track): 후속 세션 — `tests/test_u_*.py`
