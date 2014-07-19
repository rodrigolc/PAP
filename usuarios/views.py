# -*- coding: utf-8 -*-

from django.shortcuts import render
# Create your views here.
from usuarios.models import *
import time
#pagina para gerar tokens. Usada para testes.


def tokens(request):
    if request.method == 'POST':
        form = request.POST
        token = TokenConvite()
        token.token = "aaa" + str(time.time())
        token.tipo = form['tipo']
        token.save()

    return render(
        request,
        "usuarios/tokens.html",
        {
            "tokens": TokenConvite.objects.all()
        }
    )


def usuarios(request):
    if request.GET['token']:
        TokenConvite.objects.get(token=request.GET['token'])

    return render(
        request,
        "usuarios/usuarios.html", {
        "token": TokenConvite,
        }
    )
