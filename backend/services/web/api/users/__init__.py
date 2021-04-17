BASE_ROUTE = 'users'


def register_routes(api, root='api'):
    """
    Register all User Resources.

    :param api: RestX Api instance
    :type api: Api
    :param root: base route part
    :type root: str
    """
    from .controller import api as location_api

    api.add_namespace(location_api, path=f'/{root}/{BASE_ROUTE}')
