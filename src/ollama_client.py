import requests
from .config import OLLAMA_URL, MODEL_NAME

class OllamaClient:
    def generate(self, prompt: str) -> str:
        payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
        response = requests.post(OLLAMA_URL, json=payload, timeout=300)
        response.raise_for_status()
        return response.json()["response"]
