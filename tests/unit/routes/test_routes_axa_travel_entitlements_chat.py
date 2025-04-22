import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from routes.axa_travel_entitlements_chat import router  # adjust if the route file has a different name

# Set up FastAPI app for testing
app = FastAPI()
app.include_router(router)
client = TestClient(app)

# Sample chat request
def sample_chat_request():
    return {
        "messages": [
            {"role": "user", "content": "What is the travel reimbursement policy?"}
        ]
    }

def test_valid_travel_entitlements_chat():
    response = client.post("/axa-hr/travel-entitlements-chat", json=sample_chat_request())

    assert response.status_code == 200
    response_data = response.json()

    assert "role" in response_data
    assert "content" in response_data
    assert response_data["role"] == "assistant"
    assert isinstance(response_data["content"], str)
    assert len(response_data["content"]) > 0

def test_missing_messages_field():
    # Missing `messages` field entirely
    response = client.post("/axa-hr/travel-entitlements-chat", json={})
    assert response.status_code == 422  # Unprocessable Entity

def test_empty_messages_list():
    # Provide an empty message list
    response = client.post("/axa-hr/travel-entitlements-chat", json={"messages": []})
    assert response.status_code == 400
    # This depends on how your code handles an empty list
    # You might want to add validation for empty messages in `ChatRequest`
