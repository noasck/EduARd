from marshmallow import Schema, fields


class FileSchema(Schema):
    id = fields.Number(attribute='id')
    filename = fields.String(attribute='filename')
