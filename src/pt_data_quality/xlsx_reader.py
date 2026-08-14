from __future__ import annotations

import re
import zipfile
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL = "http://schemas.openxmlformats.org/package/2006/relationships"


def _column_index(cell_ref: str) -> int:
    match = re.match(r"([A-Z]+)", cell_ref or "")
    if not match:
        return 0
    value = 0
    for char in match.group(1):
        value = value * 26 + (ord(char) - ord("A") + 1)
    return value - 1


def _text_nodes(node: ET.Element) -> str:
    return "".join(t.text or "" for t in node.iter(f"{{{MAIN}}}t"))


class XlsxWorkbook:
    """Small, dependency-free, read-only XLSX reader for repository tables.

    The repository intentionally uses plain tabular sheets. This reader supports
    shared strings, inline strings, booleans, numbers and cached formula values.
    It does not attempt to implement the full Excel calculation model.
    """

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self._zip = zipfile.ZipFile(self.path)
        self._shared_strings = self._load_shared_strings()
        self._sheet_paths = self._load_sheet_paths()

    def close(self) -> None:
        self._zip.close()

    def __enter__(self) -> "XlsxWorkbook":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    @property
    def sheet_names(self) -> list[str]:
        return list(self._sheet_paths)

    def _load_shared_strings(self) -> list[str]:
        try:
            xml = self._zip.read("xl/sharedStrings.xml")
        except KeyError:
            return []
        root = ET.fromstring(xml)
        return [_text_nodes(si) for si in root.findall(f"{{{MAIN}}}si")]

    def _load_sheet_paths(self) -> dict[str, str]:
        workbook = ET.fromstring(self._zip.read("xl/workbook.xml"))
        rels = ET.fromstring(self._zip.read("xl/_rels/workbook.xml.rels"))
        targets: dict[str, str] = {}
        for rel in rels.findall(f"{{{PKG_REL}}}Relationship"):
            targets[rel.attrib["Id"]] = rel.attrib["Target"]

        result: dict[str, str] = {}
        sheets = workbook.find(f"{{{MAIN}}}sheets")
        if sheets is None:
            return result
        for sheet in sheets.findall(f"{{{MAIN}}}sheet"):
            name = sheet.attrib["name"]
            rid = sheet.attrib.get(f"{{{REL}}}id")
            target = targets.get(rid or "")
            if not target:
                continue
            if target.startswith("/"):
                path = target.lstrip("/")
            else:
                path = "xl/" + target.lstrip("/")
            path = re.sub(r"/\./", "/", path)
            result[name] = path
        return result

    def _cell_value(self, cell: ET.Element) -> Any:
        cell_type = cell.attrib.get("t")
        if cell_type == "inlineStr":
            inline = cell.find(f"{{{MAIN}}}is")
            return _text_nodes(inline) if inline is not None else ""

        value_node = cell.find(f"{{{MAIN}}}v")
        if value_node is None:
            formula = cell.find(f"{{{MAIN}}}f")
            return None if formula is not None else None
        raw = value_node.text or ""

        if cell_type == "s":
            try:
                return self._shared_strings[int(raw)]
            except (ValueError, IndexError):
                return raw
        if cell_type == "b":
            return raw == "1"
        if cell_type in {"str", "e"}:
            return raw

        try:
            number = float(raw)
            return int(number) if number.is_integer() else number
        except ValueError:
            return raw

    def rows(self, sheet_name: str) -> list[list[Any]]:
        path = self._sheet_paths[sheet_name]
        root = ET.fromstring(self._zip.read(path))
        sheet_data = root.find(f"{{{MAIN}}}sheetData")
        if sheet_data is None:
            return []
        result: list[list[Any]] = []
        for row in sheet_data.findall(f"{{{MAIN}}}row"):
            cells: dict[int, Any] = {}
            max_col = -1
            for cell in row.findall(f"{{{MAIN}}}c"):
                idx = _column_index(cell.attrib.get("r", ""))
                cells[idx] = self._cell_value(cell)
                max_col = max(max_col, idx)
            if max_col < 0:
                result.append([])
            else:
                result.append([cells.get(i) for i in range(max_col + 1)])
        return result
