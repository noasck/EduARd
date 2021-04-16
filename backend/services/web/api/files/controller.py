import os
from http import HTTPStatus
from typing import List

import werkzeug
from flask import send_from_directory
from flask_accepts import responds
from flask_cors import cross_origin
from flask_restx import Namespace, Resource, abort, reqparse

from ..project.injector import Injector
from .schema import FileSchema
from .service import AliasGenerator, File, FileService, IFile

app = Injector.app
media_folder = app.config['MEDIA_FOLDER']

file_upload = reqparse.RequestParser()
file_upload.add_argument(
    'file',
    type=werkzeug.datastructures.FileStorage,
    location='files',
    required=True,
    help='Source file',
)

api = Namespace(
    'files',
    description='Ns contains media control routes',
    decorators=[cross_origin()],
)


@api.route('/')
class FileResource(Resource):
    """Files."""

    @responds(schema=FileSchema(many=True), api=api)
    def get(self) -> List[File]:
        """Get all files list."""
        return FileService.get_all()

    @responds(schema=FileSchema, api=api)
    @api.expect(file_upload)
    def post(self):
        """Post new File to server media storage."""
        args = file_upload.parse_args()
        if args['file']:
            filename, file_extension = os.path.splitext(args['file'].filename)
            alias = AliasGenerator.random_string_generator() + file_extension
            destination = os.path.join(media_folder, alias)
            if not os.path.exists(media_folder):
                os.makedirs(media_folder)
            args['file'].save(destination)
            return FileService.create(IFile(filename=alias))
        else:
            abort(HTTPStatus.NOT_FOUND.value, message='File not sent')


@api.route('/<path:filename>')
class FileNameResource(Resource):

    @api.response(
        HTTPStatus.OK.value,
        'Returns file to download from storage media',
    )
    def get(self, filename):
        """Get file from the storage."""
        file_instance = werkzeug.utils.secure_filename(filename)
        return send_from_directory(media_folder, file_instance)

    def delete(self, filename):
        """Delete File from storage."""
        file_instance = werkzeug.utils.secure_filename(filename)
        if FileService.delete_by_filename(file_instance):
            os.remove(os.path.join(media_folder, filename))
