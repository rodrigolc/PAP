# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from pages import views

urlpatterns = patterns('',
                       url(r'^(?P<pagina>[^/]+)/$', views.index),
                       url(r'^(?P<pagina>[^/]+)/(?P<aba>[^/]+)/', views.aba)
                       )
