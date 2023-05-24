from rest_framework.routers import DefaultRouter

from user_view import UserView
from django.urls import path

# 创建路由
urlpatterns = [
    path('api/auth/', UserView.as_view())
]

# router = DefaultRouter()
# router.register('user', UserView, base_name='user')
# urlpatterns.append(router.urls)
