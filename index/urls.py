"""futures URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^$', index),
    url(r'about', about),
    url(r'list', list),
    url(r'introduce', introduce),
    url(r's_article', s_article),
    url(r'b_article', b_article),
    url(r'fee', fee),
    url(r'join', Join.as_view()),
    url(r'search', search),
]