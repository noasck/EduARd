from typing import List

from flask import jsonify, request
from flask_accepts import accepts, responds
from flask_cors import cross_origin
from flask_restx import Namespace, Resource, abort
from flask_jwt_extended import get_jwt_claims, jwt_required

from .model import Timeline
from .schema import TimelineSchema
from .service import TimelineService
from ..pups.service import PupService

api = Namespace(
    'timelines',
    description='Ns with Location entity',
    decorators=[cross_origin()],
)


@api.route('/')
class TimelineResource(Resource):
    """Timeline."""

    @accepts(schema=TimelineSchema, api=api)
    @responds(schema=TimelineSchema, api=api)
    @api.doc(security='loggedIn')
    @jwt_required
    def post(self) -> Timeline:
        """Create new Timeline instance."""
        claim = get_jwt_claims()
        user_id = int(claim['id'])
        if PupService.has_permission(user_id, request.parsed_obj['pup_id']):
            return TimelineService.create(request.parsed_obj)
        else:
            abort(403)


@api.route('/<int:pup_id>')
@api.param('pup_id', 'Pup db ID for getting timelines')
class LocationIdResource(Resource):

    @responds(schema=TimelineSchema(many=True), api=api)
    def get(self, pup_id: int):
        """Get Timelines for specific pup."""
        return TimelineService.get_by_pup_id(pup_id)
