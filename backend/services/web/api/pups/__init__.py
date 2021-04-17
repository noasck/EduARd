from flask_restx import Api

BASE_ROUTE = 'pups'
BASE_ROUTE_2 = 'subscriptions'


def register_routes(api: Api, root: str = 'api'):
    """
    Register all Pups Resources.
    :param api: RestX Api instance
    :type api: Api
    :param root: base route part
    :type root: str
    """
    from .controller import api as pups_api
    from .controller import sub_api

    api.add_namespace(pups_api, path=f'/{root}/{BASE_ROUTE}')
    api.add_namespace(sub_api, path=f'/{root}/{BASE_ROUTE_2}')
