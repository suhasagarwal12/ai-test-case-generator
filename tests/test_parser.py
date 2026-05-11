from src.parser import parse_response

def test_parse_response():
    raw = '{"test_cases": [{"id": "TC001", "title": "Login", "expected_result": "Success", "priority": "High", "steps": [], "preconditions": ""}]}'
    result = parse_response(raw)
    assert result["test_cases"][0]["id"] == "TC001"
