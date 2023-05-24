from django.http import JsonResponse
from rest_framework.views import APIView
from user_models import UserModels


class UserView(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        try:
            user_name = request._request.POST.get('user_name')
            obj = UserModels.objects.filter(username=user_name, password=user_name).first()
            if not obj:
                ret['code'] = 1010,
                ret['msg'] = "用户名或密码错误"

            ret['msg'] = "用户登录成功"
        except Exception as e:
            pass
        return JsonResponse(ret)
