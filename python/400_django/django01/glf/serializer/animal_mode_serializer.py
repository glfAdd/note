from rest_framework import serializers
from glf.models.animal_mode import AnimalModel


class AnimalModelSerializer(serializers.ModelSerializer):
    """
    Serializer 序列化的每个字段都要自己写

    ModelSerializers 继承于 Serializer, 相比其父类
    1.根据指定的Model自动检测并生成序列化的字段，不需要提前定义；
    2.自动为序列化生成校验器；
    3.自动实现了create()方法和update()方法。
    """
    class Meta:
        # 1. 指定序列化检测的模型
        model = AnimalModel

        # 2. 序列换检测的字段, __all__ 表示所有字段
        # filter = '__all__'
        filter = ('animal_name', 'status')

        # 2. 不序列换的字段
        # exclude = ('status',)
