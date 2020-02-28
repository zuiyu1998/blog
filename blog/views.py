from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from .models import BigTopic, Topic, Article


# 首页
def index(request):
    # big_topic_list = BigTopic.objects.all().order_by('id')
    article_list = Article.objects.all()
    return render(request, 'index.html', locals())


# 按主题获得文章列表
def get_article_list_by_topic(request, topic):
    # big_topic_list = BigTopic.objects.all().order_by('id')
    title = '主题'
    article_list = get_list_or_404(Article, topic__name=topic)
    return render(request, 'article_list.html', locals())


# 按标题获得文章列表
def get_article_list_by_tag(request, tag):
    # big_topic_list = BigTopic.objects.all().order_by('id')
    title = '标签'
    article_list = get_list_or_404(Article, tag__name=tag)
    return render(request, 'article_list.html', locals())
