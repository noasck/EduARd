from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy


class DatabaseSetup(object):
    """Database administration logic."""

    @classmethod
    def set_up_db(cls, app: Flask, db: SQLAlchemy):
        """
        Create all db tables.

        :param app: main Flask app.
        :type app: Flask
        :param db: db connection instance.
        :type db: SQLAlchemy
        """
        app.logger.info('Creating db tables...')
        db.session.remove()
        db.create_all()
        db.session.commit()

    @classmethod
    def tear_down_db(cls, app: Flask, db: SQLAlchemy):
        """
        Delete all db tables.

        :param app: main Flask app.
        :type app: Flask
        :param db: db connection instance.
        :type db: SQLAlchemy
        """
        app.logger.info('Removing db tables...')
        db.session.remove()
        db.drop_all()
        db.session.commit()

    @classmethod
    def add_cli(cls, app: Flask, db: SQLAlchemy, manager: Manager):
        """
        Register CLI commands for db manipulation.

        :param manager: Flask-Script manager.
        :type manager: Manager
        :param app: main Flask app.
        :type app: Flask
        :param db: db connection instance.
        :type db: SQLAlchemy
        """
        @manager.command
        def set_up():
            """Create all ab tables and seed values."""
            DatabaseSetup.set_up_db(app, db)

        @manager.command
        def tear_down():
            """Drop all ab tables."""
            DatabaseSetup.tear_down_db(app, db)
