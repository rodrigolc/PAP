# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from usuarios import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^token_page$', views.index, name='token_page')
)