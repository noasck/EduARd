from marshmallow import Schema, fields, validate


class PupSchema(Schema):
    id = fields.Number(attribute='id')
    name = fields.String(attribute='name')
    video_filename = fields.String(attribute='video_filename')
    join_code = fields.String(attribute='join_code')
    created_at = fields.Number(attribute='created_at')
