from django.urls import path, include
from . import views


urlpatterns = [
    # 首页
    path(r'', views.index, name='index'),
    # 按主题分类
    path(r'topic/<str:topic>/', views.get_article_list_by_topic, name='topic'),
    path(r'tag/<str:tag>/', views.get_article_list_by_tag, name='tag')
]