import os

basedir = os.path.abspath(os.path.dirname(__file__))

# TODO: rewrite and remove config to yml. Add validation,


class Config(object):
    API_TITLE = 'Take Me To AR API'  # noqa: WPS115
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # noqa: WPS115
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # noqa: WPS115
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')  # noqa: WPS115
    FLASK_ENV = os.getenv('FLASK_ENV')  # noqa: WPS115
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/project/media"  # noqa: WPS115,WPS237,E501
    INIT_DB = bool(os.getenv('DB_INIT'))  # noqa: WPS115
