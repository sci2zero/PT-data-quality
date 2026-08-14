from __future__ import annotations

from pathlib import Path
from typing import Any

from .model import Repository, Row
from .xlsx_reader import XlsxWorkbook


def _normalise_header(value: Any) -> str:
    return str(value).strip() if value is not None else ""


def _records(book: XlsxWorkbook, sheet_name: str, key_field: str) -> list[Row]:
    rows = book.rows(sheet_name)
    if not rows:
        return []
    headers = [_normalise_header(v) for v in rows[0]]
    records: list[Row] = []
    for row_number, values in enumerate(rows[1:], start=2):
        data = {headers[i]: values[i] if i < len(values) else None for i in range(len(headers)) if headers[i]}
        if data.get(key_field) not in (None, ""):
            records.append(Row(data=data, sheet=sheet_name, row_number=row_number))
    return records


def load_repository(xlsx_path: str | Path, schema: dict[str, Any]) -> Repository:
    sheets = schema["sheets"]
    with XlsxWorkbook(xlsx_path) as book:
        missing = [spec["name"] for spec in sheets.values() if spec["name"] not in book.sheet_names]
        if missing:
            raise ValueError(f"Missing required XLSX sheets: {', '.join(missing)}")

        metadata_rows = _records(book, sheets["repository_metadata"]["name"], sheets["repository_metadata"]["key_field"])
        metadata = {str(r.get("property")): r.get("value") for r in metadata_rows}

        kwargs: dict[str, Any] = {"metadata": metadata}
        for logical_name, spec in sheets.items():
            if logical_name == "repository_metadata":
                continue
            kwargs[logical_name] = _records(book, spec["name"], spec["key_field"])
        return Repository(**kwargs)
