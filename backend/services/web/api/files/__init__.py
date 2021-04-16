BASE_ROUTE = 'files'


def register_routes(api, root='api'):
    """
    Register all Files Resources.

    :param api: RestX Api instance
    :type api: Api
    :param root: base route part
    :type root: str
    """
    from .controller import api as files_api

    api.add_namespace(files_api, path=f'/{root}/{BASE_ROUTE}')
