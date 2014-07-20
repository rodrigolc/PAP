# -*- coding: utf-8 -*-

from django.shortcuts import render
# Create your views here.
from usuarios.models import *
import time


#pagina para gerar tokens. Usada para testes. por enquanto. haha.
#/usuarios/tokens/
def tokens(request):
    if request.method == 'POST':
        form = request.POST
        token = TokenConvite()
        token.token = "aaa" + str(time.time())
        token.tipo = form['tipo']
        token.save()

    return render(
        request,
        "usuarios/tokens/tokens.html",
        {
            "tokens": TokenConvite.objects.all()
        }
    )


#/usuarios/usuarios/
def usuarios(request):
    if request.GET['token']:
        TokenConvite.objects.get(token=request.GET['token'])

    return render(
        request,
        "usuarios/usuarios/usuarios.html", {
        "token": TokenConvite,
        }
    )


#/usuarios/cadastro/
def cadastro(request):
    #GET = pagina de cadastro
    if request.method == "GET":
        if 'token' in request.GET:
            return render(
                request,
                "usuarios/cadastro/cadastro.html", {
                "token": request.GET['token'],
                }
            )

        else:
            return render(
                request,
                "usuarios/cadastro/token_invalido.html"
            )
    elif request.method == "POST":
        pass
        #pass pra compilar, aqui fica a logica do cadastro, quando recebe
        #os dados do form de cadastro
