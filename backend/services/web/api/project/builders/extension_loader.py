from flask import Flask
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, MigrateCommand
from flask_restx import Api
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

from ..builders.singleton import singleton


class ModulesSetup(object):
    """Setups all app modules."""

    _authorizations = {
        'loggedIn': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
        },
    }

    @classmethod
    @singleton('jwt')
    def configure_jwt(cls, app: Flask) -> JWTManager:
        """Configure JSON web token plugin."""
        return JWTManager(app)

    @classmethod
    @singleton('db')
    def configure_db(cls, app: Flask) -> SQLAlchemy:
        """Configure SQLAlchemy ORM plugin."""
        return SQLAlchemy(app)

    @classmethod
    @singleton('ma')
    def configure_ma(cls, app: Flask) -> Marshmallow:
        """Configure Marshmallow plugin."""
        return Marshmallow(app)

    @classmethod
    @singleton('api')
    def configure_api(cls, app: Flask) -> Api:
        """Configure Flask RestX plugin."""
        doc = '/'
        if app.config['FLASK_ENV'] == 'production':
            doc = False

        return Api(
            app,
            app.config['API_TITLE'],
            doc=doc,
            authorizations=cls._authorizations,
        )

    @classmethod
    def configure_health_route(cls, app: Flask):
        """
        Add /health route to check server status.

        :param app: main Flask app.
        """
        @app.route('/health', methods=['GET'])
        def health():
            return 'Healthy'

    @classmethod
    def configure_fm(cls, app, db):
        """Create Flask-Migrate plugin."""
        return Migrate(app, db)

    @classmethod
    def configure_manager(cls, app: Flask) -> Manager:
        """Configure Flask-Script plugin Manager."""
        manager = Manager(app)
        manager.add_command('db', MigrateCommand)
        return manager
