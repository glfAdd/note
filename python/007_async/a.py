async def async_generator():
    yield 1

print(async_generator().send(None))