from django.contrib import admin
from .models import BigTopic, Topic, Author, Tag, Article


admin.site.register(BigTopic)
admin.site.register(Topic)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Article)