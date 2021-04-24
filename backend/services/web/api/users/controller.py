from typing import List

from flask import jsonify, request
from flask_accepts import accepts, responds
from flask_cors import cross_origin
from flask_jwt_extended import create_access_token  # noqa: WPS318
from flask_restx import Namespace, Resource, abort

from .controller_identity import verify_token, get_payload
from .schema import UserSchema
from .service import User, UserService

api = Namespace(
    'users',
    description='Ns responsible for User entity management and auth',
    decorators=[cross_origin()],
)

#: TODO: google auth


@api.route('/')
class UserResource(Resource):
    """Users."""

    @responds(schema=UserSchema(many=True), api=api)
    def get(self) -> List[User]:
        """Get all users."""
        return UserService.get_all()


@api.route('/login/')
class LoginResource(Resource):

    def get(self):
        """Get internal API token from Google-token."""
        identity = get_payload()
        print(identity)
        return identity


@api.route('/login/<string:token>')
@api.param('token', 'Client Id or Client Token from Google or Facebook')
class UserLoginResource(Resource):
    """Providing User auth and private data."""

    # TODO: refactor - make 2 GET routes for fb and google with OWN SCHEMA.

    @api.doc(responses={
        403: 'Invalid email',
        200: '{status: OK, access_token: token}',
    })
    def get(self, token: str):
        """Get internal API token from Google-token."""
        identity = verify_token(token)
        if identity:
            usr = UserService.get_or_new_by_email(identity)
            access_token = create_access_token(identity=usr)
            ret = {'status': 'OK', 'access_token': access_token}

            return jsonify(ret)
        return abort(403, message='Forbidden!')  # noqa: WPS432

    # Todo: implement user fb-auth


@api.route('/<int:user_id>')
@api.param('userId', 'User db ID')
class UserIdResource(Resource):

    @responds(schema=UserSchema, api=api)
    def get(self, user_id: int):
        """Get specific User instance."""
        return UserService.get_by_id(user_id)

    def delete(self, user_id: int):
        """Delete single User."""
        deleted_id = UserService.delete_by_id(user_id)

        return jsonify({'status': 'Success', 'id': deleted_id})
