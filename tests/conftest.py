import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from sandbox.main import get_application


@pytest.fixture
def app() -> FastAPI:
    return get_application()


@pytest.fixture
def test_client(app: FastAPI) -> TestClient:
    return TestClient(app)
