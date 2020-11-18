from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK


def test_random_user_route(test_client: TestClient) -> None:
    response = test_client.get("/random/user")
    assert response.status_code == HTTP_200_OK
