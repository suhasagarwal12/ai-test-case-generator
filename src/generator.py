from .ollama_client import OllamaClient
from .prompt_builder import build_prompt
from .parser import parse_response
from .exporter import export_json, export_markdown, export_excel

class TestCaseGenerator:
    def __init__(self):
        self.client = OllamaClient()

    def generate(self, requirement: str):
        prompt = build_prompt(requirement)
        raw_response = self.client.generate(prompt)
        data = parse_response(raw_response)
        export_json(data)
        export_markdown(data)
        export_excel(data)
        return data
