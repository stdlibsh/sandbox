from fastapi import APIRouter

from sandbox.models import User
from sandbox.services import get_random_user

router = APIRouter()


@router.get("/random/user", response_model=User, tags=["random"])
def random_user_route() -> User:
    return get_random_user()
