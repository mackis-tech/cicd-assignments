import pytest
from httpx import AsyncClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from web_app import app  # assuming main.py contains FastAPI app


@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(base_url="http://localhost:8000") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI"}

@pytest.mark.asyncio
async def test_read_item():
    async with AsyncClient(base_url="http://localhost:8000") as ac:
        name = "test"
        response = await ac.get(f"/hello/{name}")
        
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, test!"}
