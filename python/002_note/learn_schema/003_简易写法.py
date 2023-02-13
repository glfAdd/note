from schema import Schema, Or, And

# Schema({Or("name1", "name2"): str}).validate({"name1": "a", "name2": 1})

schema2 = {
    Or('id', 'name'): And(str, lambda x: 2 <= len(x), error="id error"),
    'other': And(list, [{
        "a": And(int, error='error a'),
        # "b": And(int, error='error b')
    }], lambda x: 0 < len(x), ignore_extra_keys=True, error='error other')
}

d = {
    'id': 't1',
    'name': "a111",
    'other': [
        {"a": 1, "b": 2},
        {"a": 1, "b": 2},
        {"a": 1, "b": 2}
    ]
}
a = Schema(schema2, ignore_extra_keys=True).validate(d)
