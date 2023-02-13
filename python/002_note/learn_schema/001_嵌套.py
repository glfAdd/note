from schema import Schema, And

schema2 = {
    "id": And(int, lambda x: 1 <= x, error="id error"),
    "name": And(str, error="name test"),
    'other': And(list, [{
        "a": And(int, error='error a'),
        "b": And(int, error='error b')
    }], lambda x: 0 < len(x), ignore_extra_keys=True, error='error other')
}

d = {
    'id': 123,
    'name': "aaa",
    'other': [
        {"a": 1, "b": 2},
        {"a": 1, "b": 2},
        {"a": 1, "b": 2}
    ]
}

a = Schema(schema2, ignore_extra_keys=True).validate(d)
print(123)
