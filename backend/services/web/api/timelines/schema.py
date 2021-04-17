from marshmallow import Schema, fields, validate


class TimelineSchema(Schema):
    id = fields.Number(attribute='id')
    seconds = fields.Number(attribute='seconds')
    model_filename = fields.String(attribute='model_filename')
    pup_id = fields.Number(attribute='pup_id')
