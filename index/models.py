#coding: utf-8
from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.

AIM_TYPE = (
    (1, u'业务办理'),
    (2, u'活动报名'),
    (3, u'路过，想了解一下'),
    (4, u'其他'),
)

CONTENT_POS = (
    (0, u'首页轮播图文字'),
    (1, u'关于我们'),
    (2, u'加入我们上方文字'),
    (3, u'加入我们下方文字'),
    (4, u'主页右下角文字'),
    (5, u'导航右上方文字')
)

TEXT_POS = (
    (0, u'个股期权文字'),
    (1, u'导航右上角文字'),
)


class Author(models.Model):
    name = models.CharField(u'作者名', max_length=100)
    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name

class Key_word(models.Model):
    name = models.CharField(u"关键词", max_length=20)
    class Meta:
        abstract = True
    def __unicode__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(u"标题", max_length=100)
    content = UEditorField(u'内容', max_length=100000)
    summary = models.TextField(u"摘要", max_length=10000)
    create_date = models.DateField(u'创建时间', auto_now_add=True, editable=True)
    isPublic = models.BooleanField(u'是否发布', default=True)
    author = models.ForeignKey(Author)
    class Meta:
        abstract = True
    def __unicode__(self):
        return self.title

class Search_keyword(Key_word):
    class Meta:
        verbose_name = '研究资讯关键词'
        verbose_name_plural = verbose_name

class Base_keyword(Key_word):
    class Meta:
        verbose_name = '基础知识关键词'
        verbose_name_plural = verbose_name

class Search_article(Article):
    keyword = models.ManyToManyField(Search_keyword)
    isHighLight = models.BooleanField('是否为要闻', default=False)
    class Meta:
        verbose_name = '研究资讯文章'
        verbose_name_plural = verbose_name

class Base_article(Article):
    keyword = models.ManyToManyField(Base_keyword)
    isGuide = models.BooleanField('是否为业务指南', default=False)
    class Meta:
        verbose_name = '基础知识文章'
        verbose_name_plural = verbose_name

class Introduce_Keyword(Key_word):
    class Meta:
        verbose_name = "业务信息关键词"
        verbose_name_plural = verbose_name

class Fee_Keyword(Key_word):
    class Meta:
        verbose_name = "费率关键词"
        verbose_name_plural = verbose_name

class Content(models.Model):
    title = models.CharField(u"标题", max_length=100)
    content = UEditorField(u'内容', max_length=100000)
    def __unicode__(self):
        return self.title

class Introduce_content(Content):
    keyword = models.ManyToManyField(Introduce_Keyword)
    class Meta:
        verbose_name = '业务信息页面内容'
        verbose_name_plural = verbose_name

class Fee_content(Content):
    keyword = models.ManyToManyField(Fee_Keyword)
    class Meta:
        verbose_name = '费率页面内容'
        verbose_name_plural = verbose_name

class Join_form(models.Model):
    name = models.CharField(u"姓名", max_length=100)
    aim = models.IntegerField(u"目的", choices=AIM_TYPE)
    phone = models.CharField(u"电话", max_length=11)
    place = models.CharField(u"地址", max_length=10000)
    others = models.CharField(u"其他", max_length=50000)
    isRead = models.BooleanField(u"是否已读", default=False)
    create_date = models.DateField(u"创建时间", auto_now_add=True, editable=False)
    class Meta:
        verbose_name = '加入我们提交内容'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name + "/" + self.create_date.strftime('%Y-%m-%d') + "/" + (u"已读" if self.isRead else u"未读"  )

class Friend_link(models.Model):
    link_name = models.CharField(u'友链名', max_length=100)
    link_url = models.URLField(u'链接')
    isShow = models.BooleanField(u'是否展示', default=True)
    class Meta:
        verbose_name = '友情链接管理'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.link_name

class Img_all(models.Model):
    name = models.CharField(u'图片名', max_length=100)
    img_url = models.ImageField(u'图片')
    link = models.URLField(u'对应链接')
    class Meta:
        verbose_name = '所有图片'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name

class Index_img(models.Model):
    place_name = models.CharField(u'图片位置', max_length=100)
    img = models.ManyToManyField(Img_all)
    class Meta:
        verbose_name = '首页图'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.place_name

class Page_content(models.Model):
    title = models.CharField(u'标题', max_length=100)
    content = UEditorField(u'内容', max_length=200000)
    position = models.IntegerField(u'所在位置', choices=CONTENT_POS)
    class Meta:
        verbose_name = '页面内容'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return CONTENT_POS[self.position][1]

class Page_text(models.Model):
    content = models.TextField(u'内容', max_length=200000)
    position = models.IntegerField(u'所在位置', choices=TEXT_POS)
    class Meta:
        verbose_name = '页面内容（纯文字）'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return TEXT_POS[self.position][1]



class Spider_info(models.Model):
    keywords = models.CharField(u'关键词（英文逗号分隔，别超过四个关键词）', max_length=1000)
    description = models.TextField(u'描述', max_length=1000)
    class Meta:
        verbose_name = '推广信息'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return u'推广信息'