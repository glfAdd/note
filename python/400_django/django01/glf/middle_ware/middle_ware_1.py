from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class Middleware01(MiddlewareMixin):
    def process_request(self, request):
        """request 请求到达 Django 之后

        :param request:
        :return:
        """
        print('request  01')

    def process_view(self, request, view_func, view_args, view_kwargs):
        """view 视图之前

        :param request:
        :param view_func:
        :param view_args:
        :param view_kwargs:
        :return:
        """
        print('process_view  01')

    def process_response(self, request, response):
        """
        views 处理request后，返回HttpResponse对象。该方法可以对HttpResponse对象进行修改
        :param request:
        :param response:
        :return:
        """
        print('response 01')
        return response

    def process_exception(self, request, exception):
        """处理 view 抛出的异常

        :param request:
        :param exception:
        :return:
        """
        print(exception)
        return HttpResponse('view error')
