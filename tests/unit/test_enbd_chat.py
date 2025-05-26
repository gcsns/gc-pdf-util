import pytest
from unittest.mock import Mock, patch
import sys

sys.path.append("../src")

from chat_request import ChatRequest, ChatItem
from enbd_chat import product_query
from agno.models.message import Message

@pytest.fixture
def mock_request():
    return ChatRequest(messages=[
        ChatItem(role="user", content="Tell me about credit cards"),
        ChatItem(role="assistant", content="What would you like to know?"),
        ChatItem(role="user", content="What are the benefits?")
    ])

@pytest.fixture
def mock_agent_response():
    return Message(role="assistant", content="Here are the credit card benefits...")

def test_product_query(mock_request, mock_agent_response):
    with patch('enbd_chat.Agent') as MockAgent:
        # Configure mock agent
        mock_agent_instance = Mock()
        mock_agent_instance.run.return_value = mock_agent_response
        MockAgent.return_value = mock_agent_instance

        # Call function
        result = product_query(mock_request)

        # Verify results
        assert isinstance(result, ChatItem)
        assert result.role == "assistant"
        assert result.content == mock_agent_response.content

        # Verify Agent was created with correct params
        MockAgent.assert_called_once()
        args, kwargs = MockAgent.call_args
        assert kwargs['name'] == "Prodcut Query Agent"
        assert 'system_message' in kwargs
        assert 'model' in kwargs

def test_product_query_message_formatting(mock_request):
    with patch('enbd_chat.Agent') as MockAgent:
        mock_agent_instance = Mock()
        mock_agent_instance.run.return_value = Message(role="assistant", content="test")
        MockAgent.return_value = mock_agent_instance

        product_query(mock_request)

        # Verify messages were formatted correctly
        args, kwargs = mock_agent_instance.run.call_args
        messages = kwargs['messages']
        assert all(isinstance(msg, Message) for msg in messages)
        assert len(messages) == len(mock_request.messages)
        assert all(msg.type == "text" for msg in messages)

def test_product_query_empty_messages():
    empty_request = ChatRequest(messages=[])
    with patch('enbd_chat.Agent') as MockAgent:
        mock_agent_instance = Mock()
        mock_agent_instance.run.return_value = Message(role="assistant", content="")
        MockAgent.return_value = mock_agent_instance

        result = product_query(empty_request)
        assert isinstance(result, ChatItem)
        assert result.role == "assistant"
        assert result.content == ""