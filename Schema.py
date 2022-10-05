from marshmallow import Schema, fields


class RequestData(Schema):
    cmd1 = fields.Str()
    value1 = fields.Str()
    cmd2 = fields.Str()
    value2 = fields.Str()


