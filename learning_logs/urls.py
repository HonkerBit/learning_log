""" 定义 learning_logs 的 URL 模式 """
from django.urls import path, include
from . import views

urlpatterns = [
    # 主页
    path( '', views.index, name = 'index' ),

    # 显示所有的主题
    path( r'topics/',views.topics, name='topics' )
]
app_name = 'learning_logs'