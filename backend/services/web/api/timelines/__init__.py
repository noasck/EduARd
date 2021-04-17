from flask_restx import Api

BASE_ROUTE = 'timelines'


def register_routes(api: Api, root: str = 'api'):
    """
    Register all Pups Resources.
    :param api: RestX Api instance
    :type api: Api
    :param root: base route part
    :type root: str
    """
    from .controller import api as timelines_api

    api.add_namespace(timelines_api, path=f'/{root}/{BASE_ROUTE}')
