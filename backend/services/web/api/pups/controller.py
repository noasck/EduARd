from typing import List

from flask import jsonify, request
from flask_accepts import accepts, responds
from flask_cors import cross_origin
from flask_restx import Namespace, Resource, abort
from flask_jwt_extended import get_jwt_claims, jwt_required

from .interface import IPup
from .model import Pup
from .schema import PupSchema
from .service import PupService


api = Namespace(
    'pups',
    description='Ns with Pup entity',
    decorators=[cross_origin()],
)

sub_api = Namespace(
    'subscription',
    description='Ns with User subscriptions.',
    decorators=[cross_origin()],
)


@api.route('/')
class PupResource(Resource):
    """Pups."""

    @responds(schema=PupSchema(many=True), api=api)
    @api.doc(security='loggedIn')
    @jwt_required
    def get(self) -> List[Pup]:
        """Get all Pups."""
        return PupService.get_all()

    @accepts(schema=PupSchema, api=api)
    @responds(schema=PupSchema, api=api)
    @api.doc(security='loggedIn')
    @jwt_required
    def post(self) -> Pup:
        """Create Pup instance."""
        claim = get_jwt_claims()
        user_id = int(claim['id'])
        new_pup = request.parsed_obj
        new_pup['creator_id'] = user_id
        return PupService.create(request.parsed_obj)


@api.route('/search/<string:str_to_find>')
@api.param('str_to_find', 'Part of Pup name to search')
class PupSearchResource(Resource):
    """Providing Pup search."""

    @api.doc(responses={
        200: '{"status": "Match",\n "pups": [Pup Model object]}',
        404: '{"status": "No match"}',
    })
    def get(self, str_to_find: str):
        """Get matching pups."""
        pups: List[Pup] = PupService.search_by_name(str_to_find)
        if pups:
            serialized_pups = PupSchema().dump(pups, many=True)
            return jsonify(
                {'status': 'Match', 'pups': serialized_pups},
            )
        return jsonify({'status': 'No match'}), 404


@api.route('/<int:pup_id>')
@api.param('pup_id', 'Pup db ID')
class PupIdResource(Resource):

    def get(self, pup_id: int):
        """Get count of downloads of Pup."""
        return jsonify({'count':PupService.get_downloads_count(pup_id)})

    @api.doc(responses={
        200: '{"status": "Success",\n "id": deleted_id}',
    })
    @api.doc(security='loggedIn')
    @jwt_required
    def delete(self, pup_id: int):
        """Delete single Pup."""
        claim = get_jwt_claims()
        user_id = int(claim['id'])
        if PupService.has_permission(user_id, pup_id):
            deleted_id = PupService.delete_by_id(pup_id)

            return jsonify({'status': 'Success', 'id': deleted_id})
        else:
            abort(403)

    @accepts(schema=PupSchema, api=api)
    @responds(schema=PupSchema, api=api)
    @api.doc(security='loggedIn')
    @jwt_required
    def put(self, pup_id: int):
        """Update single Pup."""
        claim = get_jwt_claims()
        user_id = int(claim['id'])
        if PupService.has_permission(user_id, pup_id):
            changes: IPup = request.parsed_obj
            loc: Pup = PupService.get_by_id(pup_id)
            return PupService.update(loc, changes)
        else:
            abort(403)


@sub_api.route('/')
class SubscriptionResource(Resource):

    @responds(schema=PupSchema(many=True), api=sub_api)
    @sub_api.doc(security='loggedIn')
    @jwt_required
    def get(self):
        """Get user saved Pups."""
        claim = get_jwt_claims()
        user_id = int(claim['id'])
        return PupService.get_subscriptions(user_id)


@sub_api.route('/<int:pup_id>')
@sub_api.param('pup_id', 'Pup db ID')
class SubscriptionsIdResource(Resource):
    @sub_api.doc(security='loggedIn')
    @jwt_required
    def post(self, pup_id: int):
        """Save Pup for current user."""
        claim = get_jwt_claims()
        user_id = int(claim['id'])
        if PupService.add_subscription_by_id(user_id, pup_id):
            return jsonify({'status': 'Success'})
        else:
            abort(404)

    @sub_api.doc(security='loggedIn')
    @jwt_required
    def delete(self, pup_id: int):
        """Delete Pup for current user from saved."""
        claim = get_jwt_claims()
        user_id = int(claim['id'])
        if PupService.delete_subscription(user_id, pup_id):
            return jsonify({'status': 'Success'})
        else:
            abort(404)


@sub_api.route('/join/<string:join_code>')
@sub_api.param('join_code', 'Pup join code to add Sub.')
class JoinCodeResource(Resource):
    @sub_api.doc(security='loggedIn')
    @jwt_required
    def post(self, join_code: str):
        """Save Pup for current user."""
        claim = get_jwt_claims()
        user_id = int(claim['id'])
        if PupService.add_subscription_by_join_code(user_id, join_code):
            return jsonify({'status': 'Success'})
        else:
            abort(404)
