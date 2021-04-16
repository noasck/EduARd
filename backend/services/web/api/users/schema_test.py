from datetime import datetime

from pytest import fixture

from ..tests.fixtures import *  # noqa
from .interface import IUser
from .model import User
from .schema import UserSchema


@fixture
def schema() -> UserSchema:
    return UserSchema()

def test_UserSchema_create(schema: UserSchema):  # noqa
    assert schema


def test_UserSchema_works(schema: UserSchema):  # noqa
    params: IUser = schema.load({
        'email': str(hash("some_str")),
        })
    widget = User(**params)

    assert widget.email == str(hash("some_str"))
