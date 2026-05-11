# AI-Powered Test Case Generator Using Ollama

Generate structured QA test cases from requirements using a local LLM running via Ollama (no API token costs).

## Features
- Local AI using Ollama
- JSON, Markdown, and Excel exports
- CLI-based usage
- Unit tests with pytest

## Tech Stack
- Python
- Ollama
- Llama 3.2 / Qwen
- Requests
- Pytest
- OpenPyXL
- Rich

## Project Structure
ai-test-case-generator/
├── src/
├── prompts/
├── samples/
├── tests/
├── output/
├── requirements.txt
├── README.md
└── .gitignore

## Quick Start
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
ollama pull llama3.2
python -m src.cli -f samples/login_requirement.txt

## Sample Input
A requirement file containing:
User stories
Acceptance criteria
Functional requirements

## Sample Output
output/test_cases.json
output/test_cases.md
output/test_cases.xlsx

## Run Tests
pytest -v

## Resume Bullet

Designed and developed a zero-cost AI-powered test case generation platform using Python and Ollama, converting requirements into structured QA test cases and exporting them to JSON, Markdown, and Excel.

## Future Enhancements
Streamlit web UI
FastAPI REST API
Jira integration
BDD scenario generation
Playwright script generation

## Author
Suhas Agarwal