from pathlib import Path

PROMPT_FILE = Path("prompts/test_case_prompt.txt")

def build_prompt(requirement: str) -> str:
    template = PROMPT_FILE.read_text(encoding="utf-8")
    return template.replace("{requirement}", requirement)
