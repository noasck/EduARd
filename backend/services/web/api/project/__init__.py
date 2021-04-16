from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix

from ..routes import register_routes
from .builders.database_loader import DatabaseSetup as DLoader
from .builders.extension_loader import ModulesSetup as MLoader
from .injector import Injector


class AppModule(object):
    """Class providing application initialization."""

    def __init__(self):
        """App module initialized with app config and Flask instance."""
        try:
            self.app = Injector.app
        except AttributeError:
            config = 'api.project.config.Config'
            app = Flask(__name__)
            app.config.from_object(config)
            app.logger.info('Application created successfully!')
            app.wsgi_app = ProxyFix(app.wsgi_app)

            self.app = app
            Injector.inject(self.app, to='app')

            self._configure_plugins()

    def _configure_plugins(self):
        """Configure main modules and extensions."""
        # Extensions modules
        MLoader.configure_jwt(self.app)
        db: SQLAlchemy = MLoader.configure_db(self.app)
        api: Api = MLoader.configure_api(self.app)
        MLoader.configure_ma(self.app)

        # Adding /health route
        MLoader.configure_health_route(self.app)

        # Registering all modules
        register_routes(api=api)

        # Adding CORS policy
        CORS(self.app)

        # Register migrations and CLI
        MLoader.configure_fm(self.app, db)
        self.manager: Manager = MLoader.configure_manager(self.app)

        # Register database brute CLI commands
        DLoader.add_cli(self.app, db, self.manager)

        self.app.logger.info('Application initialization finished!')
