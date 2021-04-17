from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    id = fields.Number(attribute='id')
    email = fields.String(attribute='email')
