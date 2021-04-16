from abc import ABC, abstractmethod
from typing import Generic, List, Type, TypeVar

from ..injector import Injector

Model = TypeVar('Model')
Interface = TypeVar('Interface')


class AbstractService(ABC, Generic[Model, Interface]):
    """Class implements operations over an instance."""

    _db = Injector.db

    @classmethod
    @abstractmethod
    def model(cls) -> Type[Model]:
        """Resolve model class."""

    @classmethod
    def get_all(cls) -> List[Model]:
        """
        Get all Model instances from database.

        :return: all existing Model instances.
        :rtype: List[Model]
        """
        return cls.model().query.all()

    @classmethod
    def get_by_id(cls, instance_id: int) -> Model:
        """
        Get Model instance with specific id.

        :param instance_id: id of required instance.
        :type instance_id: int
        :return: Model instance with specific id
        :rtype: Model
        """
        return cls.model().query.get_or_404(instance_id)

    @classmethod
    def update(cls, instance: Model, instance_upd: Interface) -> Model:
        """
        Update specific Model instance with Interface.

        :param instance: db instance to update.
        :type instance: Model
        :param instance_upd: new values of fields
        :type instance_upd: Interface
        :return: updated instance.
        :rtype: Model
        """
        instance.update(instance_upd)
        cls._db.session.commit()
        return instance

    @classmethod
    def delete_by_id(cls, instance_id: int) -> int:
        """
        Delete certain Model instance by id.

        :param instance_id: db Model instance id.
        :type instance_id: int
        :return: deleted instance id.
        :rtype: int
        """
        loc = cls.model().query.filter_by(id=instance_id).first_or_404()
        cls._db.session.delete(loc)
        cls._db.session.commit()
        return instance_id

    @classmethod
    def create(cls, new_instance: Interface) -> Model:
        """
        Create new instance.

        :param new_instance: new instance fields
        :type new_instance: Interface
        :return: new Model instance.
        :rtype: Model
        """
        loc = cls.model()(**new_instance)
        cls._db.session.add(loc)
        cls._db.session.commit()

        return loc
