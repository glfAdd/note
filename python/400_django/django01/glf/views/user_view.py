from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from glf.models.user_model import UserModels
from glf.serializer.user_serializer import UserSerializers


class UserView(APIView):
    def post(self, request, *args, **kwargs):
        # 1. orm 查询单个 UserModels
        user_name = request.data.get('user_name')
        obj_1 = UserModels.objects.filter(user_name=user_name).first()
        # 2. 序列化, 生成 python 基本数据类型
        s_1 = UserSerializers(instance=obj_1)
        # 3. 从序列化对象中取值
        print(s_1.data.get('user_name'))
        print(s_1.data.get('age'))
        # 4. dict 转为 json
        j_2 = JSONRenderer().render(s_1.data)

        # orm 查询多个
        obj_2 = UserModels.objects.all()
        # 序列化多个对象
        s_2 = UserSerializers(instance=obj_2, many=True)

        # 创建 UserModels 实例
        new_suer = UserModels.objects.create(user_name='Lucy', age=10, sex=0)
        # 保存 UserModels 实例
        new_suer.save()

        data_3 = {
            "id": 1,
            "user_name": "Tom",
            "user_name_2": "Tom",
            "user_name_3": "TomXiaoMing",
            "sex": "1",
            "sex_2": "男",
            "sex_3": "1",
            "age": 10
        }
        # 反序列化 dict
        s_3 = UserSerializers(data=data_3)
        # 当反序列化时, 调用 save() 之前必须要使用 is_valid() 方法进行校验
        # 如果校验成功返回True
        # 失败则返回False, 同时会将错误信息保存到 serializer.errors 属性中
        c = s_3.is_valid(raise_exception=True)
        e = s_3.save()

        # session
        # session 信息保存在数据库 django_session 表中
        # 能否保存在 redis 和 文件中
        request.session['test'] = 123
        # 清除 session 信息
        request.session.clear()

        return Response(s_1.data)
