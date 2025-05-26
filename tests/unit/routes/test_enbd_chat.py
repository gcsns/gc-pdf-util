from unittest.mock import patch
from fastapi.testclient import TestClient

import sys

sys.path.append("../src")

from routes.enbd_chat import router
from chat_request import ChatRequest, ChatItem

client = TestClient(router)

@pytest.fixture
def mock_response():
    return { "role": "assistant", "content": "Here are the credit card products..."}


def test_product_query_endpoint(mock_response):
    with patch("enbd_chat.product_query", return_value=mock_response):
        # Arrange
        test_request = ChatRequest(
            messages=[ChatItem(role="user", content="What are your credit card products?")]
        )
        
        # Act
        response = client.post("/enbd-chat/product-query", json=test_request.dict())
        
        # Assert
        assert response.status_code == 200
        result = response.json()
        assert isinstance(result, dict)
        assert result == mock_response
    
def test_product_query_empty_request():
    # Arrange
    test_request = ChatRequest(question="", context="")
    
    # Act
    response = client.post("/enbd-chat/product-query", json=test_request.dict())
    
    # Assert 
    assert response.status_code == 422

def test_product_query_invalid_json():
    # Act
    response = client.post("/enbd-chat/product-query", json={"invalid": "data"})
    
    # Assert
    assert response.status_code == 422

def test_product_query_valid_messages(mock_response):
    # Arrange
    messages = [ChatItem(role="user", content="Tell me about credit cards")]
    test_request = ChatRequest(messages=messages)
    
    # Act
    response = client.post("/enbd-chat/product-query", json=test_request.dict())
    
    # Assert
    assert response.status_code == 200
    result = response.json()
    assert isinstance(result, dict)
    assert mock_response == result

def test_product_query_multiple_messages(mock_response):
    # Arrange  
    messages = [
        ChatItem(role="user", content="Hi"),
        ChatItem(role="assistant", content="Hello! How can I help?"),
        ChatItem(role="user", content="What credit cards do you offer?")
    ]
    test_request = ChatRequest(messages=messages)

    # Act
    response = client.post("/enbd-chat/product-query", json=test_request.dict())
    
    # Assert
    assert response.status_code == 200
    result = response.json() 
    assert isinstance(result, dict)
    assert mock_response == result
