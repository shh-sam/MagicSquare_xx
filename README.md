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

## 프로젝트 구조

```
MagicSquare/
├── README.md
├── docs/
│   └── PRD.md                          # 제품 요구사항 (상세)
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
| [Report/01.MagicSquare_ProblemDefinition_Report.md](Report/01.MagicSquare_ProblemDefinition_Report.md) | 문제 정의 · Mom Test 워크북 |
| [Report/01.mom-test-report.md](Report/01.mom-test-report.md) | 인터뷰 상세 |

---

## 개발 (예정)

구현·테스트 코드 추가 후:

```powershell
cd c:\DEV\MagicSquare
python -m pytest -v
```

Python 버전·의존성은 `requirements.txt` 추가 시 이 README에 반영합니다.

---

## 참고

- 진짜 문제(한 문장): 채운 뒤 10선 검증 시 불일치 줄을 즉시 판정하지 못해 수동 재합산에 시간이 든다.
- ECB(`MagicSquare`, `SquareValidator`, `Solver`, `GridUI` 등)는 설계 맥락용이며, v0.1 구현 범위는 **검증 Command + Test Loop**입니다.
