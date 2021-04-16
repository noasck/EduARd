import pytest
from wsgi import start_app

from ..project.builders.database_loader import DatabaseSetup
from ..project.injector import Injector

try:
    Injector.db  # noqa: WPS428
except AttributeError:
    start_app()


@pytest.fixture
def app():
    return Injector.app


@pytest.fixture
def db(app):
    db = Injector.db
    DatabaseSetup.tear_down_db(app, db)
    DatabaseSetup.set_up_db(app, db)
    return db


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def token(client):
    from ..users.controller_test import create_token

    return create_token(client)
