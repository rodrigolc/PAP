# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from usuarios.views import *


urlpatterns = patterns('',
    url(r'^tokens/$', tokens, name='tokens')
)