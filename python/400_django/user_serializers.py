from rest_framework import serializers


class UserSerializers(serializers.Serializer):
    # name: str = serializers.CharField()
    # age: int = serializers.IntegerField()
    name: str = None
    age: int = None
