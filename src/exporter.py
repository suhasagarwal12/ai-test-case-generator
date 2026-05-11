import json
from pathlib import Path
from openpyxl import Workbook
from .config import OUTPUT_DIR

Path(OUTPUT_DIR).mkdir(exist_ok=True)

def export_json(data: dict, filename: str = "test_cases.json"):
    path = Path(OUTPUT_DIR) / filename
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path

def export_markdown(data: dict, filename: str = "test_cases.md"):
    path = Path(OUTPUT_DIR) / filename
    lines = [
        "# Generated Test Cases",
        "",
        "| ID | Title | Expected Result | Priority |",
        "|----|-------|----------------|----------|",
    ]
    for tc in data["test_cases"]:
        lines.append(
            f"| {tc['id']} | {tc['title']} | {tc['expected_result']} | {tc['priority']} |"
        )
    path.write_text("\n".join(lines), encoding="utf-8")
    return path

def export_excel(data: dict, filename: str = "test_cases.xlsx"):
    path = Path(OUTPUT_DIR) / filename
    wb = Workbook()
    ws = wb.active
    ws.title = "Test Cases"
    ws.append(["ID", "Title", "Expected Result", "Priority"])
    for tc in data["test_cases"]:
        ws.append([tc["id"], tc["title"], tc["expected_result"], tc["priority"]])
    wb.save(path)
    return path
