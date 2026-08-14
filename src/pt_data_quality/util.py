from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Iterable


def ensure_dir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def write_json(path: str | Path, value: Any) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def write_text(path: str | Path, text: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.rstrip() + "\n", encoding="utf-8")


def slug(value: str) -> str:
    result = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()
    return result or "item"


def lower_camel(parts: Iterable[str]) -> str:
    tokens: list[str] = []
    for part in parts:
        raw = [x for x in re.split(r"[^A-Za-z0-9]+", str(part)) if x]
        for token in raw:
            if token.isupper():
                tokens.extend(x.lower() for x in token.split("_") if x)
            else:
                tokens.append(token)
    if not tokens:
        return "item"
    first = tokens[0][:1].lower() + tokens[0][1:]
    return first + "".join(x[:1].upper() + x[1:] for x in tokens[1:])


def markdown_cell(value: Any) -> str:
    if value is None:
        return ""
    return str(value).replace("|", "\\|").replace("\n", "<br>")
