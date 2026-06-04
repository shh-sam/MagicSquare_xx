# MagicSquare

4×4 **부분 마방진**(빈칸 2개)을 채운 뒤, **10선**(행 4 + 열 4 + 대각 2)의 합이 **34**인지 검증하고, 틀린 줄을 **즉시 판정**하는 학습 프로젝트입니다.

**MagicSquare_1004** · PRD v0.1 · Mom Test · 세션 3 (Rule · Command · Test Loop)

---

## 배경

학습자는 마방진을 손으로 맞춘 다음 10선 합을 확인합니다. 합이 맞지 않을 때 어느 줄이 틀렸는지 바로 알기 어려워, 한 줄씩 다시 더하는 데 약 **10분**, 전체 과정에 약 **20분**이 든다는 점이 Mom Test로 확인되었습니다.  
이 저장소는 **검증·판정·재현**에 범위를 둡니다. 빈칸 자동 채우기(Solver)나 UI 전체 구현은 목표가 아닙니다.

---

## 도메인

| 항목 | 규칙 |
|------|------|
| 격자 | 4×4 |
| 숫자 | 1~16, 각 1회 (채워진 칸 기준 중복 없음) |
| 목표 합 | **34** (10선 각각) |
| 입력 예 | **빈칸 2개**인 부분 마방진 |

---

## 목표 (In Scope)

- `ValidateAllLines` — 10선 합 계산 및 34와 비교
- `ReportMismatchLines` — 불일치 시 틀린 행·열·대각 목록 (기대/실제 합)
- **Test Loop** — 동일 격자에 대해 결과 재현 (pytest)

## 비목표 (Out of Scope)

- Solver(빈칸 자동 채우기), GridUI, ECB 전체 구현
- 「마방진 프로그램을 만든다」를 제품 목표로 삼는 것

---

## 성공 기준

| ID | 기준 |
|----|------|
| AC-1 | 10선 합 검증을 한 절차로 실행 |
| AC-2 | 불일치 시 틀린 **행·열·대각** 목록 반환 |
| AC-3 | 동일 `grid` 입력 → 동일 출력 (회귀 테스트) |

---

## 8계층 (세션 3)

| 계층 | 상태 |
|------|------|
| Rule | 구현 대상 |
| Command | `ValidateAllLines`, `ReportMismatchLines` |
| (Skill) | 선택 (줄 합·라벨) |
| Test Loop | pytest |
| Entity / Boundary / Solver | 이후 세션 |

---

## TDD RED 체크리스트

**Phase:** RED — 실패 테스트만 작성 (`src/` 수정은 GREEN부터). 상세: [docs/TDD_RED_TodoList.md](docs/TDD_RED_TodoList.md)

**권장 순서:** B-2 (`D-01`~`D-08`) → B-3 (`D-LOC`) → Track A → B-1 (Out of Scope)

### Track B-2 — Logic · 세션 3 In Scope (우선)

| ID | RED 할 일 | 완료 |
|----|-----------|:----:|
| D-01 | `tests/test_d_constants.py` — `MagicConstant` SSOT, pytest **FAIL** | [ ] |
| D-02 | `tests/test_d_line_sum.py` — 단일 줄 합, pytest **FAIL** | [ ] |
| D-03 | `tests/test_d_validate.py` — `ValidateAllLines` 전선 통과, pytest **FAIL** | [ ] |
| D-04 | `tests/test_d_validate.py` — `ValidateAllLines` 불일치, pytest **FAIL** | [ ] |
| D-05 | `tests/test_d_report.py` — `ReportMismatchLines` → `[]`, pytest **FAIL** | [ ] |
| D-06 | `tests/test_d_report.py` — 단일 줄 불일치 `(line_id, expected, actual)`, pytest **FAIL** | [ ] |
| D-07 | `tests/test_d_report.py` — 복수 줄 불일치, pytest **FAIL** | [ ] |
| D-08 | `tests/test_d_regression.py` — 동일 grid → 동일 출력 (AC-3), pytest **FAIL** | [ ] |
| — | `python -m pytest tests/test_d_*.py -v` — B-2 묶음 전부 FAIL/ImportError 확인 | [ ] |

### Track B-3 — Logic · 빈칸 위치 (FR-LOC-01)

| ID | RED 할 일 | 완료 |
|----|-----------|:----:|
| D-LOC-01 | `tests/entity/test_d_loc_01.py` — G1 → `[(1,1), (3,1)]` (0-index, row-major), pytest **FAIL** | [ ] |
| D-LOC-02 | G1 → `len(result) == 2`, pytest **FAIL** | [ ] |
| D-LOC-03 | G2 → `[(0,2), (2,3)]`, pytest **FAIL** | [ ] |
| — | `reference.md`에 `D-LOC-01`~`03` 등록 | [ ] |
| — | `python -m pytest tests/entity/test_d_loc_01.py -v` — 묶음 FAIL 확인 | [ ] |
| — | `/red-skeleton` — 테스트 스켈레톤만 생성 (구현 없음) | [ ] |

### Track A — UI / Boundary (후속)

| ID | RED 할 일 | 완료 |
|----|-----------|:----:|
| U-IN-01 | `grid=None` → **E003**, pytest **FAIL** | [ ] |
| U-IN-02 | `grid=3×4` → **E001**, pytest **FAIL** | [ ] |
| U-IN-03 | 빈칸 0개 → **E003**, pytest **FAIL** | [ ] |
| U-OUT-01 | 유효 G1 → `len(result)==6` (`int[6]`), pytest **FAIL** | [ ] |
| U-FLOW-02 | `grid=None` → `execute()` 0회, pytest **FAIL** | [ ] |
| — | `tests/test_u_*.py` RED 스켈레톤 · `reference.md` U-* 등록 · ECB import 검토 | [ ] |

### Track B-1 — Logic · 전체 ECB (Out of Scope · 요청 시만)

- [ ] **D-LOC-01** — `find_blank_coords(G1)` → `[(2,2), (3,3)]` (1-index)
- [ ] **D-MIS-01** — `find_not_exist_nums(G1)` → `[7, 10]`
- [ ] **D-VAL-01** — `is_magic_square(G0)` → `True`
- [ ] **D-SOL-01** — `solution(G1)` Step A 성공

### RED 공통 (Logic · Boundary)

- [ ] Arrange: `MagicConstant` import — 리터럴 `34`/`16`/`4`/`0` 금지
- [ ] 각 테스트 docstring/`@pytest.mark`에 Test ID 명시
- [ ] Logic Track: Domain Mock 없음 · entity에 E001~E005 분기 없음
- [ ] GREEN/REFACTOR는 별 사이클 (assert 완화·skip·xfail·삭제 금지)

---

## 프로젝트 구조

```
MagicSquare/
├── README.md
├── docs/
│   ├── PRD.md                          # 제품 요구사항 (상세)
│   └── TDD_RED_TodoList.md             # Dual-Track RED To-Do (SSOT)
├── Report/
│   ├── 01.mom-test-report.md           # STEP 1 Mom Test
│   └── 01.MagicSquare_ProblemDefinition_Report.md
└── prompting/                          # Cursor 대화 export
```

---

## 문서

| 문서 | 설명 |
|------|------|
| [docs/PRD.md](docs/PRD.md) | 기능 요구(FR)·수용 기준(AC)·R-G-I-O |
| [docs/TDD_RED_TodoList.md](docs/TDD_RED_TodoList.md) | Dual-Track RED To-Do · fixture · 사이클 순서 |
| [Report/01.MagicSquare_ProblemDefinition_Report.md](Report/01.MagicSquare_ProblemDefinition_Report.md) | 문제 정의 · Mom Test 워크북 |
| [Report/01.mom-test-report.md](Report/01.mom-test-report.md) | 인터뷰 상세 |

---

## 개발

RED 단계는 위 [TDD RED 체크리스트](#tdd-red-체크리스트)를 따릅니다. 테스트 추가 후:

```powershell
cd c:\DEV\MagicSquare
# Logic — 세션 3 (B-2)
python -m pytest tests/test_d_*.py -v
# Logic — 빈칸 위치 (B-3)
python -m pytest tests/entity/test_d_loc_01.py -v
# 전체
python -m pytest -v
```

Python 버전·의존성은 `requirements.txt` 추가 시 이 README에 반영합니다.

---

## 참고

- 진짜 문제(한 문장): 채운 뒤 10선 검증 시 불일치 줄을 즉시 판정하지 못해 수동 재합산에 시간이 든다.
- ECB(`MagicSquare`, `SquareValidator`, `Solver`, `GridUI` 등)는 설계 맥락용이며, v0.1 구현 범위는 **검증 Command + Test Loop**입니다.
