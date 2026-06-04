"""Golden Master approval — fixed text format for int[6] and error codes."""

from __future__ import annotations

import os
from pathlib import Path

import pytest

GOLDEN_DIR = Path(__file__).resolve().parent / "golden"


def format_golden(actual: list[int] | str) -> str:
    """Serialize approved output. int[6] 1-index or boundary error code (E001..E007)."""
    if isinstance(actual, str):
        code = actual.strip().upper()
        if not (len(code) == 4 and code.startswith("E") and code[1:].isdigit()):
            raise TypeError(f"Expected error code E001..E007, got {actual!r}")
        return f"error\n{code}\n"
    if isinstance(actual, (list, tuple)) and len(actual) == 6 and all(
        isinstance(x, int) for x in actual
    ):
        return "int[6]\n" + ",".join(str(x) for x in actual) + "\n"
    raise TypeError(f"Expected int[6] or error code str, got {type(actual).__name__}: {actual!r}")


def assert_matches_golden(actual: list[int] | str, relative: str) -> None:
    """Compare actual to tests/golden/{relative}; update when UPDATE_GOLDEN=1."""
    golden_path = GOLDEN_DIR / relative
    serialized = format_golden(actual)

    if os.environ.get("UPDATE_GOLDEN") == "1":
        golden_path.parent.mkdir(parents=True, exist_ok=True)
        golden_path.write_text(serialized, encoding="utf-8")
        return

    if not golden_path.is_file():
        pytest.fail(f"Golden file missing: {golden_path} (run with UPDATE_GOLDEN=1 to create)")

    expected = golden_path.read_text(encoding="utf-8")
    if serialized != expected:
        pytest.fail(
            f"Golden mismatch: {golden_path}\n"
            f"--- expected ---\n{expected}"
            f"--- actual ---\n{serialized}"
        )
