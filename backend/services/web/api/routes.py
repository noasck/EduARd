from flask_restx import Api

from .files import register_routes as add_file_routing
from .users import register_routes as add_user_routing
from .pups import register_routes as add_pups_routing
from .timelines import register_routes as add_timeline_routing


def register_routes(api: Api):
    """
    Register all application RESTX Resources.

    :param api:  RestX Api instance
    :type api: Api
    """
    add_user_routing(api)
    add_file_routing(api)
    add_pups_routing(api)
    add_timeline_routing(api)
