from marshmallow import Schema, fields


class PersonSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    nat = fields.Str()
    gender = fields.Str()
    registered = fields.Str()
    picture = fields.Str()
    phone = fields.Str()
    cell = fields.Str()
    login = fields.Str()
    location = fields.Str()
    id = fields.Str()
    email = fields.Str()
    dob = fields.Str()
