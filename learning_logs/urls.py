""" 定义 learning_logs 的 URL 模式 """
from django.urls import path, include
from . import views

urlpatterns = [
    # 主页
    path( '', views.index, name = 'index' ),
]
app_name = 'learning_logs'