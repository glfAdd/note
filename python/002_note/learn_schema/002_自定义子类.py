from schema import Schema, Optional


class EventSchema(Schema):

    def validate(self, data, _is_event_schema=True):
        data = super(EventSchema, self).validate(data, _is_event_schema=False)
        if _is_event_schema and data.get("minimum", None) is None:
            data["minimum"] = data["capacity"]
        return data


a = {
    str: EventSchema({
        "capacity": int,
        Optional("minimum"): int,  # default to capacity
    })
}

events_schema = Schema(a)

b = {
    'event1': {
        'capacity': 1
    },
    'event2': {
        'capacity': 2,
        'minimum': 3
    }
}
events = events_schema.validate(b)

assert events['event1']['minimum'] == 1  # == capacity
assert events['event2']['minimum'] == 3
