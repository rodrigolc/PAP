# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from pages import views

urlpatterns = patterns('',
                       url(r'^/$', views.index),
                       url(r'^(?P<aba>[^/]+)/', views.aba)
                       )
