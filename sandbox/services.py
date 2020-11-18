from faker import Faker

from sandbox.models import User

fake = Faker()


def get_random_user() -> User:
    return User(
        email=fake.ascii_safe_email(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
    )
