import random
import string
from ..project.abstract.abstract_service import AbstractService
from .interface import IPup
from .model import Pup
from typing import List
from time import time


def random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


class PupService(AbstractService[Pup, IPup]):
    """Class implements Pup db operations."""

    @classmethod
    def model(cls):
        """
        Resolve Location model class.
        :return: Location Type.
        :rtype: type
        """
        return Pup

    @classmethod
    def get_by_join_code(cls, join_code: str) -> Pup:
        return Pup.query.filter_by(join_code=join_code).all()

    @classmethod
    def get_by_name(cls, name: str) -> Pup:
        return Pup.query.filter_by(name=name).all()

    @classmethod
    def get_authored_by(cls, user_id: int) -> List[Pup]:
        return Pup.query.filter_by(creator_id=user_id).all()

    @classmethod
    def create(cls, new_instance: IPup) -> Pup:
        join_code = random_word(6)
        while len(PupService.get_by_join_code(join_code)) != 0:
            join_code = random_word(6)
        loc = cls.model()(
            join_code=join_code,
            created_at=int(time()),
            **dict(new_instance),
        )
        cls._db.session.add(loc)
        cls._db.session.commit()

        return loc

    @classmethod
    def search_by_name(cls, str_to_find):
        return Pup.query.filter(
            Pup.name.ilike(f'%{str_to_find}%'),
        ).all()

    @classmethod
    def has_permission(cls, user_id, pup_id):
        return user_id == PupService.get_by_id(pup_id).creator_id

    @classmethod
    def get_all(cls) -> List[Pup]:
        """
        Get all Model instances from database.

        :return: all existing Model instances.
        :rtype: List[Model]
        """
        return cls.model().query.order_by(Pup.created_at.desc()).all()
