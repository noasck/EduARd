from datetime import datetime

from pytest import fixture

from ..tests.conftest import *  # noqa
from .model import User


@fixture
def user() -> User:
    return User(email=str(hash("some_str")))


def test_create_model(user: User):
    assert user
