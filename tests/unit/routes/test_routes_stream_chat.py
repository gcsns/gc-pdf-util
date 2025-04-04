import pytest
from unittest.mock import patch
from fastapi import FastAPI, status
from httpx import AsyncClient, ASGITransport

from routes.stream_chat import router

# Create a minimal app for testing just the router
test_app = FastAPI()
test_app.include_router(router)


@pytest.mark.asyncio
async def test_valid_query_agent():
    async def mock_completion_stream(_):
        yield {"answer": "Hello"}
        yield {"answer": "World"}

    with patch("chatbot.agent.completion_stream", side_effect=mock_completion_stream):
        payload = {
            "messages": [
                {"role": "user", "question": "Hi"},
                {"role": "assistant", "question": "Hello!"}
            ]
        }

        transport = ASGITransport(app=test_app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            response = await ac.post("/stream_chat/query-agent", json=payload)

        assert response.status_code == status.HTTP_200_OK
        content = b"".join([chunk async for chunk in response.aiter_bytes()])
        assert b"Hello" in content
        assert b"World" in content