# GREEN PASS — D-LOC-01

**Phase:** GREEN · **Track:** Logic · **Layer:** entity · **Test ID:** D-LOC-01  
**일자:** 2026-06-04 · **브랜치:** `green`

## 통과 기준

| 항목 | 결과 |
|------|------|
| `test_d_loc_01_blank_coords_row_major` | PASS |
| `find_blank_coords(grid_g1)` | `[(2, 2), (3, 3)]` (1-index, row-major) |
| ECB | entity E001~E005 없음 · boundary/control import 없음 |
| MagicConstant | `entity/constants.py` SSOT |

## Golden Master (AC-3 · FR-4.3 기초)

승인 baseline: [`tests/golden/d_loc_01_g1_blank_coords.golden.json`](../tests/golden/d_loc_01_g1_blank_coords.golden.json)

재생성 시 사용자 승인 후 diff 검토 (Hook 설계 예정).

## pytest (가상환경)

```powershell
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
python -m pytest tests/entity/test_d_loc_01.py -v
```

## 구현 파일

- `src/entity/constants.py`
- `src/entity/location.py` — `find_blank_coords()`
- `tests/entity/test_d_loc_01.py`
- `tests/conftest.py` — G1 fixture, `src` path bootstrap

## 다음

- **REFACTOR** (선택): 중복·네이밍 정리, 동작 불변
- **RED:** D-LOC-02, D-LOC-03
