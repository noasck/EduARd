from datetime import datetime
from typing import List

from flask_sqlalchemy import SQLAlchemy

from ..tests.fixtures import *  # noqa
from .interface import IUser
from .model import User
from .service import UserService


def test_get_all(db: SQLAlchemy):
    admin: User = User(id=1,
                       email=str(hash('example1@mail.ex')),
    )
    u1: User = User(id=2,
                    email=str(hash('example2@mail.ex')),
    )
    u2: User = User(id=3,
                    email=str(hash('example3@mail.ex')),
    )
    db.session.add(admin)
    db.session.add(u1)
    db.session.add(u2)
    db.session.commit()

    results: List[User] = UserService.get_all()

    assert len(results) == 3
    assert all((admin in results, u1 in results, u2 in results))


def test_get_by_id(db: SQLAlchemy):
    u1: User = User(
        id=1,
        email=str(hash('example2@mail.ex')),
    )
    u2: User = User(
        id=2,
        email=str(hash('example3@mail.ex')),
    )
    db.session.add(u1)
    db.session.add(u2)
    db.session.commit()

    result1: User = UserService.get_by_id(1)
    result2: User = UserService.get_by_id(2)

    assert u1 == result1
    assert u2 == result2


def test_update(db: SQLAlchemy):
    u1: User = User(
        id=2,
        email=str(hash('example1@mail.ex'))
    )
    db.session.add(u1)
    db.session.commit()

    upd: IUser = IUser(email=str(hash('new_email@mail.ex')))
    UserService.update(u1, upd)

    result: User = UserService.get_by_id(u1.id)

    assert result.email == str(hash('example1@mail.ex'))


def test_delete_by_id(db: SQLAlchemy):
    u1: User = User(
        id=2,
        email=str(hash('example2@mail.ex')),
    )
    u2: User = User(
        id=3,
        email=str(hash('example3@mail.ex')),
    )

    db.session.add(u1)
    db.session.add(u2)
    db.session.commit()

    UserService.delete_by_id(u1.id)

    result = User.query.all()

    assert len(result) == 1
    assert u2 in result
    assert u1 not in result


def test_get_or_new():

    u1 = UserService.get_or_new_by_email('example3@mail.ex')
    u2 = UserService.get_or_new_by_email('example3@mail.ex')

    assert u1 == u2
