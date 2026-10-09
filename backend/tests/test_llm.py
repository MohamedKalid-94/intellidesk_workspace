# backend/tests/test_llm.py
from services.llm import complete

def test_complete_returns_text():
    result = complete("Say hi in one word")
    assert isinstance(result, str)
    assert len(result) > 0