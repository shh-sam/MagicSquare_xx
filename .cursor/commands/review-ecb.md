# ECB · 계약 리뷰 — 코드 수정 금지

MagicSquare_1004 **ECB·도메인 계약**만 검사한다. **소스·테스트·설정 파일을 수정하지 않는다.** 위반은 표로만 보고한다.

## 필수 선언

**응답 첫 줄**에 아래 형식을 반드시 선언한다:

```
Phase: review | Layer: (전체) | Track: Logic+UI | Scope: ECB·계약
```

---

## 절차 (읽기 전용)

1. **범위 스캔** — `src/magicsquare/{entity,control,boundary}/`, `tests/test_d_*.py`, `tests/test_u_*.py` (없으면 “미구현”으로 표기).
2. **SSOT 확인** — `.cursorrules`, `docs/PRD.md`, `.cursor/skills/magic-square-tdd/SKILL.md`.
3. **체크 5항** — 아래 [검사 항목](#검사-항목)을 각각 조사한다 (grep·import·Mock·리터럴·E코드 분기).
4. **표 작성** — [보고 형식](#보고-형식)의 표만 출력한다. 수정안·패치·PR 제안은 **요청 시에만**.
5. **pytest** — 실행은 선택(계약 위반과 무관한 실패는 별도 표 “테스트 상태”에만 기록).

---

## 검사 항목

### 1. ECB import 방향

| 계약 | 허용 | 위반 |
|------|------|------|
| 레이어 흐름 | `boundary → control → entity` | `entity`/`control` → `boundary` |
| boundary import | `control` (및 표준 라이브러리) | `entity` 직접 import |
| control import | `entity` | `boundary` import |
| entity import | 표준 라이브러리만 | `magicsquare.*` 등 프로젝트 `*` import |

**조사:** 각 레이어 `*.py`의 `import` / `from … import` 목록을 파일·줄 단위로 기록.

---

### 2. Entity — E001~E005 처리 금지

| 계약 | 허용 (entity) | 위반 (entity) |
|------|----------------|---------------|
| 오류 코드 | 순수 도메인(합·10선·불일치 줄·빈칸 채움) | `E001`~`E005` 문자열·enum·분기·raise·return |
| 검증 책임 | — | 입력 형식·경계·개수·중복 등 **Boundary/Control** 책임을 entity에서 수행 |

**E001~E005 (Boundary 전용 — entity에서 생성·처리 금지):**

| 코드 | 의미 (계약 요약) |
|------|------------------|
| E001 | 입력/격자 형식 오류 |
| E002 | 좌표·인덱스 범위 오류 |
| E003 | 빈칸 개수·0 규칙 위반 |
| E004 | 1~16 중복·누락 |
| E005 | 기타 경계·유효성 검증 |

> E006~E007은 Boundary 전용(UI·I/O 등). **entity/control에서 Boundary 오류 코드를 생성하면 위반.**

**조사:** `entity/` 내 `E001`~`E005`, `raise ValueError` 등이 **입력 검증** 목적인지, boundary 전용 오류 반환인지 구분.

---

### 3. `int[6]` · 1-index 좌표

| 계약 | 기대 |
|------|------|
| Solver 출력 | `int[6]` = `[r1, c1, n1, r2, c2, n2]` |
| 좌표 | **1-index** — 행·열 `1`~`4` (0-index API·테스트 기대값 금지) |
| 빈칸 | `0` 정확히 2개, 나머지 `1`~`16` 각 1회 |

**조사:** boundary/control의 Solver·좌표 변환, 테스트 fixture·assert에서 `0`~`3` 인덱스 사용 여부.

---

### 4. MagicConstant SSOT

| 계약 | 허용 | 위반 |
|------|------|------|
| 정의원 | `entity/constants.py` 또는 `MagicConstant` 등 **단일 SSOT** | `src/`·`tests/`에 `34`/`16`/`4`/`0` **리터럴 산재** |
| 사용 | `from … import MagicConstant` (또는 동등 SSOT) | 매직 넘버로 도메인 상수 반복 |

**조사:** `src/`, `tests/`에서 `\b34\b`, `\b16\b`, 격자 `4`, 빈칸 `0` 리터럴 — SSOT·주석·문서 문자열 제외하고 위반 목록화.

---

### 5. Logic Track — Domain Mock 금지

| 계약 | Logic (`tests/test_d_*.py`) | UI (`tests/test_u_*.py`) |
|------|-----------------------------|---------------------------|
| 호출 | entity/control **직접** | boundary만 |
| Mock | **Domain Mock 금지** (실제 객체·순수 함수) | Mock **허용** (I/O·UI 격리) |
| 우회 | stub/mock으로 entity·control GREEN 유도 금지 | Logic 테스트에 UI Mock으로 boundary 대체 금지 |

**조사:** `unittest.mock`, `pytest` fixture의 `MagicMock`/`patch`가 **entity·control·도메인 타입**을 대체하는지. `tests/test_d_*.py`만 집중.

---

## 보고 형식

아래 표를 **반드시** 채운다. 위반 0건이면 `위반` 열에 `—`, `심각도`에 `PASS`.

### 요약

| 항목 | 결과 |
|------|------|
| 검사 일시·범위 | (브랜치/경로) |
| 위반 건수 | N |
| 즉시 수정 권고 | (있으면 ID 나열, **코드는 수정하지 않음**) |

### 위반 목록 (메인)

| ID | 체크 | 파일:줄 | 위반 내용 | 계약 근거 | 심각도 |
|----|------|---------|-----------|-----------|--------|
| V-01 | import 방향 | `…` | (한 줄 요약) | `.cursorrules` ECB | BLOCKER / MAJOR / MINOR |
| V-02 | E001~E005 | `…` | entity에서 E003 분기 | entity E001~E005 금지 | BLOCKER |
| … | … | … | … | … | … |

`ID`는 `V-01`부터 순번. **체크** 열 값: `import` · `E001~E005` · `int[6]/1-index` · `MagicConstant` · `Logic Mock` 중 하나.

### 체크별 PASS/FAIL

| 체크 | 결과 | 비고 |
|------|------|------|
| import 방향 | PASS / FAIL | |
| entity E001~E005 | PASS / FAIL | |
| int[6] 1-index | PASS / FAIL / N/A | Solver·좌표 미구현 시 N/A |
| MagicConstant SSOT | PASS / FAIL | |
| Logic Track Domain Mock | PASS / FAIL / N/A | `test_d_*` 없으면 N/A |

### (선택) 테스트 상태

| 명령 | 결과 | 비고 |
|------|------|------|
| `python -m pytest tests/test_d_*.py -v` | passed / failed / skipped | 계약 리뷰와 별도 |

---

## 금지

| 금지 | 이유 |
|------|------|
| **`src/`·`tests/`·설정 수정** | 리뷰 전용 Command |
| **위반 “자동 수정”·GREEN 시도** | 별도 TDD GREEN / REFACTOR 세션 |
| **계약 외 리팩터·기능 제안을 본문에 장문으로** | 표·요약만; 상세는 사용자 요청 시 |
| **E006~E007을 entity 위반으로 오판** | entity 금지는 **E001~E005**; E006~E007은 boundary 전용 |

---

## 참고

- TDD 절차: `.cursor/skills/magic-square-tdd/SKILL.md`
- 테스트 ID: `.cursor/skills/magic-square-tdd/reference.md`
- SSOT: `.cursorrules`, `docs/PRD.md`
