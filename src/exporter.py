import io
from datetime import datetime

import pandas as pd


def to_excel(content: str) -> bytes:
    """
    Convert generated Markdown/text content into an Excel file.

    Current implementation stores the entire generated response in a single
    worksheet. This is intentionally simple and robust.

    Future enhancement:
    - Parse Markdown into structured rows
    - Create columns such as:
      Test Case ID, Scenario, Steps, Expected Result, Priority, Severity
    """

    buffer = io.BytesIO()

    df = pd.DataFrame(
        {
            "Generated Test Cases": [content],
            "Generated On": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        }
    )

    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Test Cases")

    buffer.seek(0)
    return buffer.getvalue()


def to_markdown(content: str) -> bytes:
    """
    Convert generated content to a downloadable Markdown file.
    """
    header = (
        "# AI-Generated Test Cases\n\n"
        f"_Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_"
        "\n\n---\n\n"
    )

    return (header + content).encode("utf-8")