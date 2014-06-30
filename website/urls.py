# _*_ coding: utf-8 _*_
__author__ = 'nislam <connect2nazrul@gmail.com>'
from django.conf.urls import (patterns, url)
from .views import *
urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='index')
)
