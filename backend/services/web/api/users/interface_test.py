from pytest import fixture

from ..tests.fixtures import *  # noqa
from .interface import IUser
from .model import User


@fixture
def interface() -> IUser:
    return IUser(email=str(hash("some_str")))


def test_interface_create(interface: IUser):
    assert interface


def test_interface_works(interface: IUser):
    user = User(**interface)
    assert user
