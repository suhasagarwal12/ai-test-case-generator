import json

def parse_response(response: str) -> dict:
    start = response.find("{")
    end = response.rfind("}") + 1
    if start == -1 or end == 0:
        raise ValueError("No valid JSON found in model response")
    return json.loads(response[start:end])
