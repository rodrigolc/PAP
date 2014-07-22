from widgets.models import *
from django.template.loader import render_to_string
# -*- coding: utf-8 -*-

# Criar aqui as funcoes de parsing dos widgets


def default(widget):
    return render_to_string("widgets/files/widget1.html", {})


def calendar(widget,request,obj):
    return render_to_string("widgets/files/calendar.html", obj)
