from functools import wraps
from typing import Callable

from ..injector import Injector


def singleton(instance: str = 'name') -> Callable:
    """
    Wrap injector decorator.

    :param instance: name of instance to inject
    :type instance: str
    :return: injector decorator
    :rtype: Callable
    """

    def save_to_storage(factory_method):
        """
        Decorate factory function with dependency storage.

        :param factory_method: method that supplies specific instance
        :type factory_method: Callable
        :return: wrapped function
        :rtype: Callable
        """

        @wraps(factory_method)
        def wrapper(*args, **kwargs):
            returned_instance = factory_method(*args, **kwargs)
            Injector.inject(returned_instance, to=instance)
            return returned_instance

        return wrapper

    return save_to_storage
