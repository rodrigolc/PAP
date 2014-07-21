# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from usuarios import views


urlpatterns = patterns('',
                       url(r'^tokens/$', views.tokens, name='tokens'),
                       url(r'^usuarios/$', views.usuarios, name='usuarios'),
                       url(r'^cadastro/$', views.cadastro, name='cadastro')
                       )
