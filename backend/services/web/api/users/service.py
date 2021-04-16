from typing import Optional

from ..project.abstract.abstract_service import AbstractService
from .interface import IUser
from .model import User


class UserService(AbstractService[User, IUser]):
    """Class implements Location db operations."""

    @classmethod
    def model(cls):
        """
        Resolve Location model class.

        :return: Location Type.
        :rtype: type
        """
        return User

    @classmethod
    def get_by_email(cls, email: str) -> Optional[User]:
        """
        Get certain User by email.

        :param email: user's email
        :type email: str
        :return: matched user
        :rtype: str
        """
        return User.query.filter_by(email=email).first()

    @classmethod
    def get_or_new_by_email(cls, email: str):
        """
        Get existing or create new User by received email.

        :param email: logged in users email
        :type email: str
        :return: User instance
        :rtype: str
        """
        usr = UserService.get_by_email(email)
        if not usr:
            usr = User(email=email)
            cls._db.session.add(usr)
            cls._db.session.commit()
        return usr
