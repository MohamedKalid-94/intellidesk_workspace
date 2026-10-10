from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_chat_returns_reply(monkeypatch):
    monkeypatch.setattr("routers.chat.complete", lambda prompt: "Hi.")
    response = client.post("/api/chat", json={"message": "Say hi"})
    assert response.status_code == 200
    assert response.json() == {"reply": "Hi."}


def test_chat_rejects_blank_message():
    response = client.post("/api/chat", json={"message": "   "})
    assert response.status_code == 422


def test_chat_rejects_missing_message():
    response = client.post("/api/chat", json={})
    assert response.status_code == 422


def test_chat_returns_503_when_llm_fails(monkeypatch):
    def boom(prompt):
        raise RuntimeError("provider down")

    monkeypatch.setattr("routers.chat.complete", boom)
    response = client.post("/api/chat", json={"message": "hi"})
    assert response.status_code == 503