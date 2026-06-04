---
name: magic-square-tdd
description: MagicSquare_1004 Dual-Track TDD·ECB 개발 시 Agent가 따를 절차. TDD·RED/GREEN/REFACTOR·Logic/UI Track·ValidateAllLines·ReportMismatchLines·pytest·ECB entity/control/boundary 작업 시 사용.
---

# MagicSquare TDD Skill

MagicSquare_1004 **Dual-Track TDD + ECB** 개발 절차. `.cursorrules`·`docs/PRD.md`와 충돌 시 Rules 우선.

## 언제 이 Skill을 켜는지

| 트리거 | 예 |
|--------|-----|
| 사용자가 TDD·RED/GREEN/REFACTOR·Logic/UI Track 명시 | 「D-05 RED부터」「Logic Track GREEN」 |
| entity/control/boundary 구현·테스트 작성 | `ValidateAllLines`, `ReportMismatchLines` |
| pytest 실행·회귀 확인 요청 | 「테스트 돌려줘」「D-07 통과 확인」 |
| ECB 레이어 분리·Mock 사용 여부 판단 | 「entity에 검증 넣어도 돼?」 |
| MagicSquare_1004 세션 3+ 코드 작업 | Rule·Command·Test Loop 구현 |

**켜지 않을 때:** PRD/보고서·Mom Test·`.cursorrules` 문서만 작성, git commit/push, Command 파일(별도 세션) 작업.

매 턴 선언: **Phase** (RED/GREEN/REFACTOR) · **Layer** (entity/control/boundary) · **Track** (Logic/UI) · **Test ID** (예: D-05).

---

## Logic Track vs UI Track

| 항목 | Logic Track | UI Track |
|------|-------------|----------|
| **Layer** | entity, control | boundary |
| **테스트 ID** | `D-*` | `U-*` |
| **파일** | `tests/test_d_*.py` | `tests/test_u_*.py` |
| **호출 대상** | entity/control 직접 | boundary만 |
| **Mock** | **Domain Mock 금지** | **허용** (I/O·UI 격리) |
| **세션 3 우선** | ✅ Validate / ReportMismatch | ⏸ PRD Out of Scope — 요청 없이 착수 금지 |
| **ECB import** | entity: 프로젝트 `*` import 금지 | boundary → control만 |

---

## ECB · Mock · E001~E007

| 항목 | 허용 | 금지 |
|------|------|------|
| **ECB 방향** | boundary → control → entity | entity/control → boundary 역방향 |
| **entity import** | 표준 라이브러리만 | `magicsquare.*` 등 프로젝트 `*` import |
| **E001~E007** | boundary에서 입력·형식·경계 검증·반환 | entity에서 E001~**E005** 분기·처리 |
| **E006~E007** | boundary 전용 (정의 후 SSOT) | entity/control에서 Boundary 오류 코드 생성 |
| **Logic Mock** | 실제 객체·순수 함수 | Domain Mock으로 GREEN 달성 |
| **UI Mock** | boundary 테스트에서 입출력 대역 | Logic Track 테스트에 Mock으로 entity 우회 |
| **MagicConstant** | `entity/constants.py` 등 SSOT import | 소스·테스트에 `34`/`16`/`4`/`0` 리터럴 산재 |
| **표면 문제** | 검증·판정·재현 (PRD In Scope) | Solver·GridUI·ECB 전체를 목표로 선행 구현 |
| **GREEN 수단** | 최소 구현으로 테스트 통과 | assert 완화, `@pytest.mark.skip`, `xfail`, 테스트 삭제 |

---

## RED (5~7단계)

1. **범위 확인** — PRD In Scope인지, Logic/UI Track·Layer·Test ID 확정.
2. **ID 선택** — [reference.md](reference.md)에서 다음 `D-*` (또는 `U-*`) 확인; 미등록이면 reference에 추가 후 진행.
3. **실패 테스트 작성** — `tests/test_d_*.py` (또는 `test_u_*.py`); docstring 또는 `@pytest.mark`에 ID 명시.
4. **Arrange** — Mom Test·슬라이드 격자 fixture; 상수는 `MagicConstant` import.
5. **Act / Assert** — 요구 행동·기대값을 **엄격히** 기술 (틀린 줄 ID·expected/actual 포함).
6. **RED 확인** — 아래 Test Loop의 **Phase RED** pytest 실행 → **반드시 실패** 확인.
7. **보고** — 실패 메시지·누락 구현 요약; **구현 코드는 아직 작성하지 않음**.

---

## GREEN (5~7단계)

1. **Phase 선언** — GREEN · Layer · Track · Test ID.
2. **최소 구현** — 해당 테스트를 통과하는 **가장 작은** 코드만 추가 (entity → control 순, boundary는 UI Track만).
3. **레이어 준수** — entity는 순수 도메인; E001~E005·입출력은 boundary/control에 두지 않았는지 확인.
4. **Mock 금지 (Logic)** — Domain Mock·우회 stub 없이 실제 호출 경로로 통과.
5. **GREEN 확인** — Phase GREEN pytest 실행 → **해당 ID 통과**.
6. **회귀** — `pytest tests/test_d_*.py -v` (Logic) 또는 해당 Track 전체.
7. **보고** — 추가·변경 파일, 통과 테스트 ID, 아직 RED인 후속 ID.

---

## REFACTOR (5~7단계)

1. **Phase 선언** — REFACTOR · Layer · Track.
2. **전제** — 현재 사이클 GREEN 유지; **동작 변경·새 요구 추가 금지**.
3. **대상** — 중복 제거, 네이밍, MagicConstant SSOT 정리, ECB 경계 명확화.
4. **테스트 불변** — assert 완화·skip·삭제 없이 리팩터만 수행.
5. **REFACTOR 확인** — Phase REFACTOR pytest (해당 ID + Track 전체).
6. **다음 사이클** — reference에서 다음 미구현 `D-*` → RED.
7. **보고** — 리팩터 요약, diff 범위, 전체 Logic pytest 결과.

---

## Test / Review Loop

| 시점 | 명령 | 통과 기준 |
|------|------|-----------|
| **RED 직후** | `python -m pytest tests/test_d_<file>.py::<test> -v` | **실패** (ImportError·AssertionError OK) |
| **GREEN 직후** | 동일 `-k` 또는 `::test` | **해당 ID 통과** |
| **REFACTOR 후** | `python -m pytest tests/test_d_*.py -v` | Logic Track **전부 통과** |
| **사이클 완료** | `python -m pytest -v` | D-* + (있으면) U-* 전체 |
| **UI Track (후속)** | `python -m pytest tests/test_u_*.py -v` | boundary만; Mock 허용 |

**Review Loop (완료 전 필수):**

1. Test ID ↔ 파일·함수 매핑이 [reference.md](reference.md)와 일치하는가
2. entity에 E001~E005·boundary import 없는가
3. Logic Track에 Domain Mock 없는가
4. `34`/`16`/`4`/`0` 리터럴이 MagicConstant 외부에 없는가
5. PRD Out of Scope(Solver·GridUI) 선행 구현 없는가

---

## 완료 보고 항목

사이클·기능 단위 작업 종료 시 아래 형식으로 보고:

```markdown
## TDD 완료 보고

- **Phase / Track / Layer:** REFACTOR · Logic · entity
- **Test ID:** D-05 (통과), D-06 (다음 RED 예정)
- **pytest:** `tests/test_d_validate.py` — 5 passed
- **변경 파일:** (목록)
- **ECB 준수:** entity import 금지 ✅ · E001~E005 entity 미사용 ✅
- **Mock:** Logic Track Mock 없음 ✅
- **AC 연결:** AC-1 / AC-2 / AC-3 중 해당 항목
- **미완:** (다음 RED ID 또는 Out of Scope 보류 사항)
```

---

## 참고

- 테스트 ID 목록: [reference.md](reference.md)
- SSOT: `.cursorrules`, `docs/PRD.md`, `Report/01.MagicSquare_ProblemDefinition_Report.md`
- Command 파일(`ValidateAllLines` 등 Cursor Command): **본 Skill 범위 아님** — 별도 세션
