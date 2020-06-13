""" 为应用程序 users 定义 URL 模式 """

from django.urls import path,include
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # 登录页面
    path( 'login/', LoginView.as_view(template_name='users/login.html'), name='login' ),
]

app_name = 'users'