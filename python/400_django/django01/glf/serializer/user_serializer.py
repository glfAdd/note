from rest_framework import serializers

from glf.models.user_model import UserModels


class UserSerializers(serializers.Serializer):
    # id: int = None
    # user_name: str = None
    # age: int = None

    # p1. 指定要序列化的字段
    id = serializers.IntegerField()
    user_name = serializers.CharField()
    # 用 source 执行 user_name_2 的来源, 原来的 model 里没有 user_name_2 这个字段
    user_name_2 = serializers.CharField(source='user_name')
    # 用 source 调用 model 中的函数 user_name_3() 获取值
    user_name_3 = serializers.CharField(source='get_user_name')

    sex = serializers.CharField()
    sex_2 = serializers.CharField(source='get_sex_display')
    sex_3 = serializers.CharField(source='sex')
    age = serializers.IntegerField()

    # p2
    class Meat:
        """哪些字段进行序列化"""
        model = UserModels
        filter = ('user_name', 'sex', 'age')

    # p3
    def create(self, validated_data):
        """
        反序列化时创建 model
        当执行 save() 时调用
        """
        age = validated_data.get('age') + 100
        # tmp_user = UserModels.objects.create(**validated_data)
        tmp_user = UserModels.objects.create(user_name='Lucy2', age=age, sex=0)
        return tmp_user

    # p4
    def update(self, instance, validated_data):
        """
        反序列化时创建 model
        当执行 save() 时调用
        """
        print(1111111111)
        pass
