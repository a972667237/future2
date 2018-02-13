#coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.views.generic import View
from django.http import HttpResponse

from .models import *
# Create your views here.


def index(requests):
    pageinfo = 1
    indexright = Img_all.objects.get(name="主页右下角")
    fr = Friend_link.objects.filter(isShow=True)
    hl = Search_article.objects.filter(isPublic=True, isHighLight=True).order_by('-pk')[0:5]
    info = Search_article.objects.filter(isPublic=True).order_by('-pk')[0:5]
    fi = Base_article.objects.filter(isPublic=True).order_by('-pk')[0:5]
    po = Base_article.objects.filter(isPublic=True, isGuide=True).order_by('-pk')[0:5]
    head = Page_content.objects.get(position=0)
    bannertop = Page_content.objects.get(position=5)
    power = Page_content.objects.get(position=4)
    head_img = Index_img.objects.get(id=1)
    bottom_img = Index_img.objects.get(id=2)
    return render(requests, 'index2/index.html', locals())

def about(requests):
    bannertop = Page_content.objects.get(position=5)
    pageinfo = 2
    fr = Friend_link.objects.filter(isShow=True)
    ab = get_object_or_404(Page_content, position=1)
    return render(requests, 'index2/about.html', locals())

def list(requests):
    bannertop = Page_content.objects.get(position=5)
    fr = Friend_link.objects.filter(isShow=True)
    kv = 0
    article_type = int(requests.GET.get('type', 1))
    keyword = int(requests.GET.get('keyword', 0))
    if (article_type == 1):
        hot_key = Search_keyword.objects.all()[0:6]
    else:
        hot_key = Base_keyword.objects.all()[0:6]
    pageinfo = 4 + article_type
    if keyword == 0:
        if(article_type == 1):
            article = Search_article.objects.filter(isPublic=True).order_by('-pk')
        else:
            article = Base_article.objects.filter(isPublic=True).order_by('-pk')
    else:
        if (article_type == 1):
            k = Search_keyword.objects.filter(id=keyword)
            article = Search_article.objects.filter(isPublic=True,  keyword=k).order_by('-pk')
        else:
            k = Base_keyword.objects.filter(id=keyword)
            article = Base_article.objects.filter(isPublic=True,  keyword=k).order_by('-pk')
    art_len = article.count()
    paginator = Paginator(article, 10)
    try:
        page = int(requests.GET.get('page', 1))
        article = paginator.page(page)
    except(EmptyPage, InvalidPage):
        article = paginator.page(1)
        page = 1
    art_index = page
    front = art_index - 1
    if front > 2:
        front = 2
    end = 4 - front
    if end + art_index > art_len/10 + 1:
        end = int(art_len/10 + 1 - art_index)
    page_list = range(art_index-front, art_index+end+1)
    return render(requests, 'index2/article_list.html', locals())

def introduce(requests):
    bannertop = Page_content.objects.get(position=5)
    fr = Friend_link.objects.filter(isShow=True)
    pageinfo = 4
    keyword = int(requests.GET.get('keyword', 0))
    hot_key = Introduce_Keyword.objects.all()
    if keyword == 0:
        intro = Introduce_content.objects.all()
    else:
        k = Introduce_Keyword.objects.get(id=keyword)
        intro = Introduce_content.objects.filter(keyword=k)
    return render(requests, 'index2/info.html', locals())

def s_article(requests):
    bannertop = Page_content.objects.get(position=5)
    fr = Friend_link.objects.filter(isShow=True)
    art_id = int(requests.GET.get('id'))
    article = get_object_or_404(Search_article, pk=art_id, isPublic=True)
    pageinfo = 5
    try:
        article_front = Search_article.objects.get(pk=art_id-1)
    except:
        article_front = Search_article(title="")
    try:
        article_then = Search_article.objects.get(pk=art_id+1)
    except:
        article_then = Search_article(title="")
    more_article = Search_article.objects.filter(isPublic=True, keyword__in=article.keyword.all()).exclude(id=article.id).order_by('-pk')
    more_article_temp = []
    for i in more_article:
        canSave = True
        for j in more_article_temp:
            if i.id == j.id:
                canSave = False
                break
        if canSave:
            more_article_temp.append(i)
            if len(more_article_temp) == 5:
                break
    more_article = more_article_temp
    return render(requests, 'index2/article.html', locals())

def b_article(requests):
    bannertop = Page_content.objects.get(position=5)
    fr = Friend_link.objects.filter(isShow=True)
    art_id = int(requests.GET.get('id'))
    article = get_object_or_404(Base_article, pk=art_id, isPublic=True)
    pageinfo = 6
    try:
        article_front = Base_article.objects.get(pk=art_id-1)
    except:
        article_front = Base_article(title="")
    try:
        article_then = Base_article.objects.get(pk=art_id+1)
    except:
        article_then = Base_article(title="")
    more_article = Base_article.objects.filter(isPublic=True, keyword__in=article.keyword.all()).exclude(
            id=article.id).order_by('-pk')
    more_article_temp = []
    for i in more_article:
        canSave = True
        for j in more_article_temp:
            if i.id == j.id:
                canSave = False
                break
        if canSave:
            more_article_temp.append(i)
            if len(more_article_temp) == 5:
                break
    more_article = more_article_temp
    return render(requests, 'index2/article.html', locals())

def fee(requests):
    bannertop = Page_content.objects.get(position=5)
    pageinfo = 7
    fr = Friend_link.objects.filter(isShow=True)
    keyword = int(requests.GET.get('keyword', 0))
    hot_key = Fee_Keyword.objects.all()
    if keyword == 0:
        intro = Fee_content.objects.all()
    else:
        k = Fee_Keyword.objects.get(id=keyword)
        intro = Fee_content.objects.filter(keyword=k)
    return render(requests, 'index2/info.html', locals())

class Join(View):
    def get(self, requests):
        bannertop = Page_content.objects.get(position=5)
        pageinfo = 3
        fr = Friend_link.objects.filter(isShow=True)
        po = Base_article.objects.filter(isPublic=True, isGuide=True).order_by('-pk')[0:10]
        jo_top = Page_content.objects.get(position=2)
        jo_bot = Page_content.objects.get(position=3)
        return render(requests, 'index2/join.html', locals())

    def post(self, requests):
        import re
        name = requests.POST.get('name')
        if len(name) == 0:
            return HttpResponse("必须输入名字")
        phone = requests.POST.get('phone')
        p = re.compile('^0\d{2,3}\d{7,8}$|^1[3578]\d{9}$|^147\d{8}')
        if not p.match(phone):
            return HttpResponse("手机格式有误")
        aim = requests.POST.get('aim')
        if not aim:
            return HttpResponse("必须选择一个目的")
        others = requests.POST.get('others')
        place = requests.POST.get('place')
        try:
            Join_form(name=name, phone=phone, aim=aim, others=others, place=place).save()
        except:
            return HttpResponse("不可预知的错误")
        return HttpResponse("提交成功")

def search(requests):
    bannertop = Page_content.objects.get(position=5)
    article_type = int(requests.GET.get('type', '1'))
    pageinfo = 110
    keyword = 0
    fr = Friend_link.objects.filter(isShow=True)
    kv = requests.GET.get('keyword', u'移动')
    if article_type == 1:
        article = Search_article.objects.filter(isPublic=True, keyword__name__contains=kv)
    elif article_type == 2:
        article = Base_article.objects.filter(isPublic=True, keyword__name__contains=kv)
    else:
        article_s = Search_article.objects.filter(isPublic=True, keyword__name__contains=kv)
        article_b = Base_article.objects.filter(isPublic=True, keyword__name__contains=kv)
        if article_s.count() > article_b.count():
            article = article_s
            article_type = 1
        else:
            article = article_b
            article_type = 2
    art_len = article.count()
    paginator = Paginator(article, 10)
    try:
        page = int(requests.GET.get('page', 1))
        article = paginator.page(page)
    except(EmptyPage, InvalidPage):
        article = paginator.page(1)
        page = 1
    art_index = page
    front = art_index - 1
    if front > 2:
        front = 2
    end = 4 - front
    if end + art_index > art_len / 10 + 1:
        end = int(art_len / 10 + 1 - art_index)
    page_list = range(art_index - front, art_index + end + 1)
    return render(requests, 'index2/article_list.html', locals())
