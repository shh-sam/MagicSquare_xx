# TDD RED — 실패 테스트 먼저

MagicSquare_1004 **Dual-Track TDD** — RED 단계만 수행한다. 구현 코드는 작성하지 않는다.

## 필수 선언

**응답 첫 줄**에 아래 형식을 반드시 선언한다:

```
Phase: red | Layer: entity | Track: Logic | Test ID: D-05
```

| 필드 | 값 |
|------|-----|
| **Phase** | `red` (고정) |
| **Layer** | `entity` · `control` · `boundary` 중 하나 |
| **Track** | `Logic` (D-*, entity/control) · `UI` (U-*, boundary) |
| **Test ID** | `D-*` 또는 `U-*` (예: D-05, U-01) |

---

## 절차

1. **범위·Track 확인** — PRD In Scope인지, Logic/UI Track·Layer·Test ID를 확정한다.
2. **ID 확인** — `.cursor/skills/magic-square-tdd/reference.md`에서 대상 `D-*` / `U-*`를 확인한다. 미등록이면 reference에 추가한 뒤 진행한다.
3. **AAA 테스트 작성** — `tests/` 아래에만 파일을 추가·수정한다.
   - Logic: `tests/test_d_*.py` · UI: `tests/test_u_*.py`
   - docstring 또는 `@pytest.mark`에 Test ID를 명시한다.
   - **Arrange** — Mom Test·슬라이드 격자 fixture; 상수는 `MagicConstant` import (리터럴 `34`/`16`/`4`/`0` 금지).
   - **Act** — entity/control(Logic) 또는 boundary(UI)를 **직접** 호출한다.
   - **Assert** — 기대 행동·값을 **엄격히** 기술한다 (불일치 시 line_id, expected, actual 포함).
4. **pytest FAIL 확인** — 아래 명령으로 실행하고 **반드시 실패**하는지 확인한다 (`ImportError` · `AssertionError` 모두 RED로 유효).
5. **보고** — 아래 [보고](#보고) 형식으로 마무리한다. **`src/`는 건드리지 않는다.**

---

## pytest 예시 (bash)

```bash
# Logic Track — 단일 테스트 (RED: 실패 기대)
python -m pytest tests/test_d_report.py::test_d05_all_lines_pass_returns_empty_list -v

# Logic Track — ID 키워드
python -m pytest tests/test_d_report.py -k "d05" -v

# UI Track (후속)
python -m pytest tests/test_u_boundary.py::test_u01_example -v
```

RED 직후 통과하면 **테스트가 너무 약하거나 이미 구현된 것** — assert를 강화하거나 대상 ID를 재확인한다.

---

## 보고

```markdown
## TDD RED 보고

- **Phase / Track / Layer:** red · Logic · entity
- **Test ID:** D-05
- **pytest:** `tests/test_d_report.py::test_d05_...` — **FAILED** (AssertionError: …)
- **FAIL 요약:** ReportMismatchLines 미구현 — ImportError / 기대값 불일치 등 한 줄 요약
- **변경 파일:** tests/test_d_report.py (tests/ 만)
- **다음:** GREEN — 최소 구현으로 해당 ID 통과
```

---

## 금지

| 금지 | 이유 |
|------|------|
| **`src/` 수정·추가** | RED는 실패 테스트만; 구현은 GREEN |
| **Logic Track Domain Mock** | entity/control 우회 stub·가짜 도메인 객체로 통과 유도 |
| **assert 완화·skip·xfail·테스트 삭제** | GREEN을 테스트 조작으로 달성 |
| **E001~E005를 entity에서 처리** | boundary 전용 검증 규칙 |
| **PRD Out of Scope 선행** | Solver·GridUI 등 요청 없이 착수 금지 |

Logic Track에서 UI Mock으로 boundary를 대체하지 않는다. UI Track에서만 Mock 허용.
