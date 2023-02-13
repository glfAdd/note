import schema


class EventSchema(schema.Schema):



    def validate(self, data: str, _is_event_schema=True)->None:
        """_summary_

        :param _type_ data: _description_
        :param _type_ _is_event_schema: _description_, defaults to True
        :return _type_: _description_
        """

        data = super(EventSchema, self).validate(data, _is_event_schema=False)
        if _is_event_schema and data.get("minimum", None) is None:
            data["minimum"] = data["capacity"]
        return data


events_schema = schema.Schema({
    str: EventSchema({
        "capacity": int,
        schema.Optional("minimum"): int,  # default to capacity
    })
})

text = {
    "event1": {
        "capacity": 1
    },
    "event2": {
        "capacity": 2,
        "minimum": 3
    }
}
events = events_schema.validate(text)

assert events["event1"]["minimum"] == 1  # == capacity
assert events["event2"]["minimum"] == 3
