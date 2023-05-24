from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class Middleware02(MiddlewareMixin):
    def process_request(self, request):
        print('request  02')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('process_view  02')

    def process_response(self, request, response):
        print('response 02')
        return response
