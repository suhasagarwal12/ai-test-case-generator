# AI-Powered Test Case Generator Using Ollama

Generate structured QA test cases from requirements using a local LLM running via Ollama (no API token costs).

## Features
- Local AI using Ollama
- JSON, Markdown, and Excel exports
- CLI-based usage
- Unit tests with pytest

## Quick Start
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
ollama pull llama3.2
python -m src.cli -f samples/login_requirement.txt
```
