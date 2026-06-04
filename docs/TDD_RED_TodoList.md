# TDD RED — To-Do List (Dual-Track)

**버전:** 0.1  
**일자:** 2026-06-04  
**상태:** RED 설계 확정 · 테스트·구현 미착수  
**근거:** Dual-Track TDD RED 설계표 · `.cursor/skills/magic-square-tdd/reference.md` · `docs/PRD.md` · `.cursorrules`

---

## 1. 개요

| 항목 | 내용 |
|------|------|
| **Phase** | RED (실패 테스트 먼저 — `src/` 수정은 GREEN부터) |
| **Track A** | UI / Boundary — `U-*`, `tests/test_u_*.py` |
| **Track B** | Domain / Logic — `D-*`, `tests/test_d_*.py` 또는 `tests/entity/` |
| **현재** | `tests/test_d_*.py`, `tests/test_u_*.py` **없음** — 아래 항목은 RED 스켈레톤·pytest FAIL 확인 대기 |

**우선순위 (PRD v0.1 In Scope):** Track B-2 (`D-01`~`D-08`) → Track B-3 (`D-LOC-01`~`03`) → Track A·B-1은 후속 세션 또는 명시 요청 시.

**좌표 규약 (GREEN 전 통일 필요):**

| 레이어 | 좌표 |
|--------|------|
| Boundary · Solver 출력 `int[6]` | **1-index** (행·열 1~4) |
| Entity Skill (`GetBlankCoords` 등) | RED 세션 설계: **0-index** `(row, col)` |
| 수업 슬라이드·이미지 (`find_blank_coords`) | **1-index** `[(2,2), (3,3)]` — G1 동일 격자를 0-index로는 `[(1,1), (3,1)]` |

**Boundary 오류 코드 (SSOT: `review-ecb.md`, `.cursorrules`):**

| 코드 | 의미 |
|------|------|
| E001 | 입력/격자 형식 오류 |
| E002 | 좌표·인덱스 범위 오류 |
| E003 | 빈칸 개수·0 규칙 위반 |
| E004 | 1~16 중복·누락 |
| E005 | 기타 경계·유효성 |
| E006~E007 | Boundary 전용 (UI·I/O) |

Entity는 **E001~E005 처리 금지**. Logic Track **Domain Mock 금지**.

---

## 2. Track A — UI / Boundary

**레이어:** `boundary` · **파일 예:** `tests/test_u_boundary.py` · **reference:** U-* 후속 세션

### 2.1 입력 검증 (U-IN)

- [ ] **U-IN-01** — `grid=None` → **E003** 반환 (입력 없음·null) · RED: `ModuleNotFoundError` 또는 boundary 미구현
- [ ] **U-IN-02** — `grid=3×4` → **E001** (격자 형식 오류) · RED: `AssertionError`
- [ ] **U-IN-03** — 빈칸 0개 (0이 정확히 2개가 아님) → **E003** · RED: `AssertionError`

### 2.2 출력 · 흐름 (U-OUT / U-FLOW)

- [ ] **U-OUT-01** — 유효 입력 **G1** → `len(result) == 6` (`int[6]` Solver 출력) · RED: `pytest.fail()`
- [ ] **U-FLOW-02** — `grid=None` → control/entity `execute()` **0회** · RED: `pytest.fail()`

### 2.3 Track A 공통 완료 조건

- [ ] `tests/test_u_*.py` RED 스켈레톤 작성 (`/red-skeleton` 또는 `tdd-red` 절차)
- [ ] pytest 실행 후 **의도적 FAIL** 확인 (`ImportError` / `AssertionError` / `pytest.fail` 유효)
- [ ] `reference.md`에 U-* ID 등록
- [ ] ECB 리뷰: boundary → control만 import, entity 직접 import 없음

---

## 3. Track B — Domain / Logic

**레이어:** `entity`, `control` · **Mock:** Domain Mock **금지**

### 3.1 B-1 — 전체 ECB 도메인 (설계 맥락 · PRD Out of Scope)

> Solver·`is_magic_square`·`solution` 전체는 v0.1 비목표. 테스트는 **요청·후속 세션**에서만 착수.

- [ ] **D-LOC-01** — `find_blank_coords(G1)` → `[(2,2), (3,3)]` (1-index, row-major, I6)
- [ ] **D-MIS-01** — `find_not_exist_nums(G1)` → `[7, 10]` 오름차순 (I7, I11)
- [ ] **D-VAL-01** — `is_magic_square(G0 완전)` → `True` (I1~I5)
- [ ] **D-SOL-01** — `solution(G1)` Step A 성공 (I8, `int[6]`)

### 3.2 B-2 — 세션 3 PRD In Scope (`reference.md` SSOT)

**파일 매핑:**

| ID | 파일 | 검증 대상 |
|----|------|-----------|
| D-01 | `tests/test_d_constants.py` | `MagicConstant` SSOT (34, 16, 4, 0) |
| D-02 | `tests/test_d_line_sum.py` | 단일 줄 합 (행/열/대각) |
| D-03 | `tests/test_d_validate.py` | `ValidateAllLines` — 10선 전부 34 |
| D-04 | `tests/test_d_validate.py` | `ValidateAllLines` — 불일치 존재 |
| D-05 | `tests/test_d_report.py` | `ReportMismatchLines` — 전선 통과 → `[]` |
| D-06 | `tests/test_d_report.py` | `ReportMismatchLines` — 단일 줄 불일치 |
| D-07 | `tests/test_d_report.py` | `ReportMismatchLines` — 복수 줄 불일치 |
| D-08 | `tests/test_d_regression.py` | 동일 grid → 동일 출력 (AC-3) |

**To-Do:**

- [ ] **D-01** — MagicConstant RED 테스트 · FAIL 확인
- [ ] **D-02** — 단일 줄 합 RED 테스트 · FAIL 확인
- [ ] **D-03** — `ValidateAllLines` 전선 통과 RED · FAIL 확인
- [ ] **D-04** — `ValidateAllLines` 불일치 RED · FAIL 확인
- [ ] **D-05** — `ReportMismatchLines` 빈 목록 RED · FAIL 확인
- [ ] **D-06** — `ReportMismatchLines` 단일 불일치 `(line_id, expected, actual)` RED · FAIL 확인
- [ ] **D-07** — `ReportMismatchLines` 복수 불일치 RED · FAIL 확인
- [ ] **D-08** — 회귀(동일 grid → 동일 출력) RED · FAIL 확인
- [ ] B-2 RED 묶음 pytest: `python -m pytest tests/test_d_*.py -v` (전부 FAIL 또는 ImportError)

### 3.3 B-3 — 빈칸 위치 (FR-LOC-01 · `/tdd-red` 확정 묶음)

**대상 함수:** `GetBlankCoords` · **파일 예:** `tests/entity/test_d_loc_01.py` · **conftest:** `tests/entity/conftest.py` (데이터만)

**G1 fixture (0-index):**

```
16   3   2  13
 5   0  11   8
 9   6   7  12
 4   0  14   1
```

→ 기대: `[(1,1), (3,1)]`

**G2 fixture (0-index):**

```
 1   2   0   4
 5   6   7   8
 9  10  11   0
13  14  15  16
```

→ 기대: `[(0,2), (2,3)]`

**To-Do:**

- [ ] **D-LOC-01** — G1 → `[(1,1), (3,1)]` row-major · RED: `ImportError` / `AssertionError`
- [ ] **D-LOC-02** — G1 → `len(result) == 2` · RED: `ImportError` / `AssertionError`
- [ ] **D-LOC-03** — G2 → `[(0,2), (2,3)]` · RED: `ImportError` / `AssertionError`
- [ ] `reference.md`에 `D-LOC-01`~`03` 등록
- [ ] pytest: `python -m pytest tests/entity/test_d_loc_01.py -v` — 묶음 전부 FAIL 확인
- [ ] `/red-skeleton` — 위 설계 기준 테스트 스켈레톤만 생성 (구현 없음)

### 3.4 Track B 공통 완료 조건

- [ ] Arrange: `MagicConstant` import — 리터럴 `34`/`16`/`4`/`0` 금지
- [ ] docstring 또는 `@pytest.mark`에 Test ID 명시
- [ ] entity에 E001~E005 분기 없음 (유효 fixture만 사용)
- [ ] GREEN/REFACTOR는 별 사이클 — assert 완화·skip·xfail·삭제 금지

---

## 4. 사이클 순서 (권장)

```text
1. B-2: D-01 → D-02 → D-03 → D-04 → D-05 → D-06 → D-07 → D-08  (RED 각각 → GREEN → REFACTOR)
2. B-3: D-LOC-01 → D-LOC-02 → D-LOC-03  (RED 묶음 → skeleton → GREEN)
3. Track A: U-IN → U-OUT / U-FLOW  (boundary RED, Mock 허용)
4. B-1: D-LOC/MIS/VAL/SOL  (Out of Scope — 명시 요청 시만)
```

---

## 5. 관련 문서

| 문서 | 설명 |
|------|------|
| [PRD.md](PRD.md) | In Scope / Out of Scope |
| [../.cursor/skills/magic-square-tdd/reference.md](../.cursor/skills/magic-square-tdd/reference.md) | D-* ID SSOT |
| [../.cursor/commands/tdd-red.md](../.cursor/commands/tdd-red.md) | RED 절차 |
| [../Report/01.MagicSquare_ProblemDefinition_Report.md](../Report/01.MagicSquare_ProblemDefinition_Report.md) | 문제 정의 |

---

## 6. 변경 이력

| 일자 | 변경 |
|------|------|
| 2026-06-04 | 초안 — Dual-Track RED 설계표를 To-Do List로 문서화 |
