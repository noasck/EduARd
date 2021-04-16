import re


class MetaInjector(type):
    """Storage to inject dependencies."""

    _storage = {}

    def inject(cls, instance, to: str = 'name'):
        """
        Assign internal static field to instance link.

        :param instance: instance to save in database.
        :type instance: any
        :param to: name of instance.
        :type to: str
        :raises NameError: if instance name is incorrect.
        """
        if re.match('[a-zA-Z_][a-zA-Z_0-9]*', to):
            MetaInjector._storage[to] = instance  # noqa: WPS437
        else:
            raise NameError(to, " can't be the name of injected instance.")

    def __getattr__(cls, instance_name: str):
        """
        Return saved in static field instance.

        :param instance_name: name of instance.
        :type instance_name: str
        :return: required function or instance.
        :raises AttributeError: if instance name is incorrect.
        """
        try:
            return MetaInjector._storage[instance_name]  # noqa: WPS437
        except KeyError:
            raise AttributeError(instance_name, " wasn't injected.")


class Injector(object, metaclass=MetaInjector):
    """Public interface for multitone."""
