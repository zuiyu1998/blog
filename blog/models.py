from django.db import models
from slugger import AutoSlugField


# 导航主题
class BigTopic(models.Model):
    name = models.CharField(verbose_name='导航主题', max_length=20, unique=True)

    class Meta:
        verbose_name = '导航主题'
        verbose_name_plural = verbose_name
        # ordering = ['-id']

    def __str__(self):
        return self.name


# 分类主题
class Topic(models.Model):
    name = models.CharField(verbose_name='分类主题', max_length=20, unique=True)
    big_topic = models.ForeignKey(verbose_name='导航主题', to='BigTopic', to_field='id', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '分类主题'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 作者
class Author(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField(verbose_name='作者名', max_length=10, unique=True)
    password = models.CharField(verbose_name='密码', max_length=128)
    email = models.EmailField(verbose_name='邮箱', unique=True)
    sex = models.CharField(verbose_name='性别',max_length=32, choices=gender, default='男')
    create_date = models.DateField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name
        ordering = ['create_date']

    def __str__(self):
        return self.name


# 标签
class Tag(models.Model):
    name = models.CharField(verbose_name='标签名', max_length=20, unique=True)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 博文
class Article(models.Model):
    title = models.CharField(verbose_name='文章标题', max_length=50)
    content = models.TextField(verbose_name='文章内容')
    slug = AutoSlugField(verbose_name='简短标识', populate_from='title', unique=True, max_length=50)
    author = models.ForeignKey(verbose_name='作者', to='Author', to_field='id', on_delete=models.CASCADE)
    topic = models.ForeignKey(verbose_name='主题', to='Topic', to_field='id', on_delete=models.CASCADE)
    tag = models.ManyToManyField(verbose_name='标签', to='Tag')
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['create_date']

    def __str__(self):
        return self.title
